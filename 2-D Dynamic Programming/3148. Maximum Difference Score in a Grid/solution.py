class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[inf]*n for _ in range(m)]
        res = -inf
        for i in range(m):
            for j in range(n):
                prev = min(dp[i-1][j] if i-1>=0 else inf, dp[i][j-1] if j-1>=0 else inf)
                res = max(res, grid[i][j]-prev)
                dp[i][j] = min(dp[i][j], prev, grid[i][j])
        return res
