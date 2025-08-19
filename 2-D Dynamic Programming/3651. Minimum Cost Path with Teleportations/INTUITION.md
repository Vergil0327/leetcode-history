# Intuition

一開始想到用dijkstra

```py

from collections import defaultdict
import heapq
from math import inf


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        dirs = [[0,1],[1,0]]
        m, n = len(grid), len(grid[0])

        graph = defaultdict(lambda: defaultdict(lambda: inf))

        nodes = []
        for r in range(m):
            for c in range(n):
                nodes.append([grid[r][c], r, c])
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < m and col < n:
                        graph[r,c][row,col] = grid[row][col]


        nodes.sort()
        teleport = defaultdict(lambda: defaultdict(lambda: inf))
        for i in range(len(nodes)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nodes[j][0] == nodes[i][0]:
                    teleport[nodes[i][1], nodes[i][2]][nodes[j][1], nodes[j][2]] = 0 # teleport
                    teleport[nodes[j][1], nodes[j][2]][nodes[i][1], nodes[i][2]] = 0 # teleport
                elif nodes[j][0] < nodes[i][0]:
                    teleport[nodes[i][1], nodes[i][2]][nodes[j][1], nodes[j][2]] = 0 # teleport

        min_heap = [[0, 0, 0, 0]] # cost, row, col, # of teleportation

        visited = defaultdict(lambda: inf)
        while min_heap:
            cost, r, c, numTel = heapq.heappop(min_heap)

            if r == m-1 and c == n-1: return cost
            if visited[r,c,numTel] <= cost: continue
            visited[r,c,numTel] = cost

            for (row,col) in graph[r,c]:
                heapq.heappush(min_heap, [cost+graph[r,c][row,col], row, col, numTel])
            if numTel < k:
                for (row,col) in teleport[r,c]:
                    heapq.heappush(min_heap, [cost, row, col, numTel+1])
        return -1
```

但是TLE, 後來想到top-down dp

```py
from collections import defaultdict
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        nodes = []
        for r in range(m):
            for c in range(n):
                nodes.append([grid[r][c], r, c])

        nodes.sort()
        teleport = defaultdict(set)
        for i in range(len(nodes)-1, -1, -1):
            for j in range(i-1, -1, -1):
                cost1, r, c = nodes[i]
                cost2, row, col = nodes[j]
                if cost1 == cost2:
                    teleport[r,c].add((row,col))
                    teleport[row,col].add((r,c))
                elif cost2 < cost1:
                    teleport[r,c].add((row,col))

        @cache
        def dfs(r, c, k):
            if k < 0: return inf
            if r == m-1 and c == n-1: return 0

            res = inf
            if r+1 < m:
                res = min(res, dfs(r+1, c, k) + grid[r+1][c])
            if c+1 < n:
                res = min(res, dfs(r, c+1, k) + grid[r][c+1])
            for (row,col) in teleport[r,c]:
                res = min(res, dfs(row, col, k-1))
            return res
        return dfs(0, 0, k)
```

甚至排序優化過:

```py
from collections import defaultdict
from typing import List
import bisect
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Precompute cells by value and sort unique values
        value_to_cells = defaultdict(list)
        for i in range(m):
            for j in range(n):
                value_to_cells[grid[i][j]].append((i, j))
        
        sorted_values = sorted(value_to_cells.keys())
        
        # Memoization cache: dp[i][j][k] = min cost from (i, j) with k teleports
        dp = {}
        
        def solve(i: int, j: int, k: int) -> int:
            # Base case: reached destination
            if i == m - 1 and j == n - 1: return 0
            
            # Out of bounds
            if i >= m or j >= n: return inf
            
            # Check memoized result
            state = (i, j, k)
            if state in dp: return dp[state]
            
            ans = inf
            
            # Normal move: right
            if j + 1 < n:
                cost_right = grid[i][j + 1]
                ans = min(ans, cost_right + solve(i, j + 1, k))
            
            # Normal move: down
            if i + 1 < m:
                cost_down = grid[i + 1][j]
                ans = min(ans, cost_down + solve(i + 1, j, k))
            
            # Teleportation: if k > 0, try teleporting to cells with value <= grid[i][j]
            if k > 0:
                curr_val = grid[i][j]
                # Find the largest value <= curr_val using binary search
                idx = bisect.bisect_right(sorted_values, curr_val)
                # Iterate over all valid values <= curr_val
                for val in sorted_values[:idx]:
                    for x, y in value_to_cells[val]:
                        if (x, y) != (i, j):  # Avoid teleporting to current cell
                            ans = min(ans, solve(x, y, k - 1))
            
            # Store result in memo
            dp[state] = ans
            return ans
        
        # Start from (0, 0) with k teleports
        result = solve(0, 0, k)
        return result if result != inf else -1
```

依舊TLE

這題從解答看起來得用bottom-up才能過:

### DP Definition

首先定義dp[row][col][k]: the minimum cost to reach (row, col) using *k* times teleportation at most

### base case

在不使用任何teleport的情況下的dp[row][col][0] = min(dp[row-1][col][0], dp[row][col-1][0]) + grid[row][col]

```py
# base case
dp = [[[inf] * (k+1) for _ in range(n)] for _ in range(m)]
for r in range(m):
    for c in range(n):
        if r == 0 and c == 0:
            dp[r][c][0] = 0
        else:
            if r > 0:
                dp[r][c][0] = min(dp[r][c][0], dp[r-1][c][0])
            if c > 0:
                dp[r][c][0] = min(dp[r][c][0], dp[r][c-1][0])
            dp[r][c][0] += grid[r][c]
```

那再來就是嘗試在每個`kk`次teleport情況下更新dp

- 先利用O(grid)的時間 + 排序, 以`grid[i][j]`由大到小排出前次teleport的每個位置dp state
- 由於已經由大到小排序, 那麼我們在遍歷這個順序時, 對於當前dp[row][col][kk], 他可以從先前每個`>= grid[row][col]`的狀態用teleport轉移過來. 既然要轉移, 當然是從這之中找個最小的來進行, 所以我們才紀錄一個prefix minimum `mini`.
  - 更新dp[row][col][kk] = mini
- 在嘗試完teleport之後, 我們一樣透過move down / move right來更新dp[row][col][kk] = min(dp[row-1][col][kk], dp[row][col-1][kk]) + grid[row][col]

```py
for kk in range(1, k+1):
    # teleport
    s = sorted((-grid[i][j], dp[i][j][kk-1], i, j) for j in range(n) for i in range(m))
    mini = inf
    for _, cost, r, c in s:
        mini = min(mini, cost)
        dp[r][c][kk] = mini
        
    # move down/right
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                dp[r][c][kk] = 0
            else:
                if r > 0:
                    dp[r][c][kk] = min(dp[r][c][kk], dp[r-1][c][kk] + grid[r][c])
                if c > 0:
                    dp[r][c][kk] = min(dp[r][c][kk], dp[r][c-1][kk] + grid[r][c])
```

最終答案就是: dp[m-1][n-1][k]