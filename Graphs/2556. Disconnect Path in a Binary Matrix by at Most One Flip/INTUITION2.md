# BFS

## Intuition

由於BFS會在每個位置探索所有每個可能的路

因此我們只要BFS一抵達終點就break
同時，如果在抵達終點的過程中，有任一個時刻點我們的queue裡只存在一個點，並且那個點不是起點也不是終點
那代表我們只要阻斷這個點，就無法抵達終點
因為在那個時間點時，我們能前進的路只有一條

```py
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        queue = deque([(0,0)])
        visited = [[0]*n for _ in range(m)]

        dirs = [[1, 0], [0, 1]]
        canCut = False
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == m-1 and c == n-1: break
                
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row >=m or col >= n: continue
                    if not grid[row][col]: continue
                    if visited[row][col]: continue
                    visited[row][col] = 1

                    queue.append((row, col))
            
            if len(queue) < 2:
                canCut = not queue or queue[0] not in {(0,0), (m-1, n-1)}
                break

        return canCut
```

但會錯在這個test case: `grid=[[1,1,1],[1,0,0],[1,1,1],[1,1,1]]`

這是因為我們真正想要阻斷的是能夠通往終點的點, 如果queue裡面有些點本來就不會通往(m-1, n-1)
那這些點其實從一開始就不用考慮, 放進queue裡會導致我們這條件`if len(queue) < 2`判斷錯誤

因此在這之前, 我們必須我們必須先用一次BFS, 紀錄我們從(m-1, n-1)到(0,0)的所有路徑
如果這時發現根本抵達不了, 那可以直接先返回True

然後再執行一次我們原本的BFS, 只是這次條件改成, 我們只能走在第一次BFS有經過的點上才行
因為這些點才是能通往終點的路徑, 我們block掉這些點才有意義
最後一樣判斷在每次的BFS過程中, 有沒有能block的時機點即可
```py
if len(queue) < 2:
    canCut = not queue or queue[0] not in {(0,0), (m-1, n-1)}
    break
```

> the positions in the queue might not be reachable from the dest.
> what we really want to block is the grid[i][j] which can reach destination
> thus, we BFS from (m-1, n-1) to (0, 0) first, and mark all the visited grid as `2`.
> then we BFS again from (0,0) to (m-1,n-1), just like original answer, but this time, we skip one more condition which is all the grid not visited from previous BFS.
> if this grid can't lead us to destination, we don't even need to block it.