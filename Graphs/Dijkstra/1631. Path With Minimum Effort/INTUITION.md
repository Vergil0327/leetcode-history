# Dijkstra

## Intuition

effort就相當於有加權的邊，並且沒有負權值，且要求最小的effort，因此可以用Dijkstra
用一個dp數組紀錄並更新每個點的最低effort，也相當於是visited hashset，僅有effort較低的才會加入到min heap裡

一路上取`max`更新effort，假如比dp數組裡面的值還小就更新並加入min heap，這樣抵達終點時的effort即為最小

## Complexity

- time complexity
$$O((V+E)logV)$$

# Binary Search

## Intuition

由於這題是求一個最小的effort，我們可以試著用binary search去猜這個值
因為effort越大，越容易到終點，越小則越難抵達終點
並且一定有解，所以最終會收斂到最佳解

想法是我們的search space為`[0, max(heights)]`，最小差值就是每一格值都相等，差為0，最大則應該是`最大數-0`

然後每猜一個effort，我們就看在這個effort限制下能不能抵達終點

```py
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, visited, upperbound):
            if r == ROWS-1 and c == COLS-1: return True

            visited.add((r,c))

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row >= ROWS or col<0 or col >= COLS: continue
                if (row, col) in visited: continue
                if abs(heights[row][col]-heights[r][c]) > upperbound: continue
                if dfs(row, col, visited, upperbound): return True
            return False

        l, r = 0, -inf
        for height in heights:
            for v in height:
                r = max(r, v)
        while l < r:
            mid = l + (r-l)//2
            if dfs(0, 0, set(), mid):
                r = mid
            else:
                l = mid+1
        return l
```
