class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][int(grid[0][0] > 0)] = grid[0][0]

        for r in range(m):
            for c in range(n):
                for kk in range(k+1):
                    if dp[r][c][kk] > -1:
                        if r+1 < m and (new_cost := kk+int(grid[r+1][c] > 0)) <= k:
                            dp[r+1][c][new_cost] = max(dp[r+1][c][new_cost], dp[r][c][kk] + grid[r+1][c])
                        if c+1 < n and (new_cost := kk+int(grid[r][c+1] > 0)) <= k:
                            dp[r][c+1][new_cost] = max(dp[r][c+1][new_cost], dp[r][c][kk] + grid[r][c+1])
        res = max(dp[m-1][n-1])
        return res if res > -inf else -1