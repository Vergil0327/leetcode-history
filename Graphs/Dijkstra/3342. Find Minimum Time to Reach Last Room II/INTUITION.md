# Intuition

[341. Find Minimum Time to Reach Last Room I](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/)的follow-up

由於這次每一步的時間耗費是`+1`, `+2`相互交替
所以我們可以很簡單的更改一下, 多紀錄一個變數`alt`來看當前步數耗費時間是`+1`還`+2`即可

一樣定義visited[row][col]: the minimum time to reach (row, col)

狀態變化如右: `visited[row][col] = min(visited[row][col], max(visited[r][c], moveTime[row][col])+1+alt)`

整體框架如下:

```py
def minTimeToReach(self, moveTime: List[List[int]]) -> int:
    m, n = len(moveTime), len(moveTime[0])

    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([[0, 0, 0]]) # alternating, r, c
    visited = [[inf]*n for _ in range(m)]
    visited[0][0] = 0
    while queue:
        for _ in range(len(queue)):
            alt, r, c = queue.popleft()

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row>=m or col<0 or col>=n: continue
                if visited[row][col] <= visited[r][c]+1: continue
                visited[row][col] = min(visited[row][col], max(visited[r][c], moveTime[row][col])+1+alt)
                queue.append([1-alt, row, col])

    return visited[m-1][n-1]
```

但由於這次數據規模變大, 單純BFS會超時
那要求兩位置間的最短路徑直覺會想到dijkstra algo.
所以我們僅需要將BFS改用heap來找最短路徑, 找到的第一個抵達(m-1, n-1)位置的時間即為答案

```py
pq = [[0,0,0,0]] # t, alternating, r, c
visited = set([(0,0)])
while pq:
    t, alt, r, c = heapq.heappop(pq)
    if r == m-1 and c == n-1:
        return t
    
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row<0 or row>=m or col<0 or col>=n: continue
        if (row, col) in visited: continue
        visited.add((row, col))
        tt = max(t, moveTime[row][col])+1+alt
        heapq.heappush(pq, [tt, 1-alt, row, col])
return -1
```