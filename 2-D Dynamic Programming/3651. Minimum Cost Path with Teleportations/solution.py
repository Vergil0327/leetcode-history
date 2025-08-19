from math import inf
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

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

        return dp[m-1][n-1][k]

### space-optimized

from math import inf
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 0
                else:
                    if r > 0:
                        dp[r][c] = min(dp[r][c], dp[r-1][c])
                    if c > 0:
                        dp[r][c] = min(dp[r][c], dp[r][c-1])
                    dp[r][c] += grid[r][c]

        for kk in range(k):
            s = sorted((-grid[i][j], dp[i][j], i, j) for j in range(n) for i in range(m))
            dp_next = [[inf for _ in range(n)] for _ in range(m)]
            mini = inf
            for _, cost, r, c in s:
                mini = min(mini, cost)
                dp_next[r][c] = mini
                
            for r in range(m):
                for c in range(n):
                    if r == 0 and c == 0:
                        dp_next[r][c] = 0
                    else:
                        if r > 0:
                            dp_next[r][c] = min(dp_next[r][c], dp_next[r-1][c] + grid[r][c])
                        if c > 0:
                            dp_next[r][c] = min(dp_next[r][c], dp_next[r][c-1] + grid[r][c])
            dp = dp_next
        return dp[-1][-1]