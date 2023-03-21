class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[1, 1] for _ in range(n)] for _ in range(m)] # dp[i][j]: [negative, positive]
        
        dp[0][0] = [grid[0][0], grid[0][0]]
        for i in range(1, m):
            v = dp[i-1][0][0] * grid[i][0]
            dp[i][0] = [v, v]
        for j in range(1, n):
            v = dp[0][j-1][0] * grid[0][j]
            dp[0][j] = [v, v]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j][0] = min(dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j], dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j])
                dp[i][j][1] = max(dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j], dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j])
                
        if dp[m-1][n-1][1] < 0: return -1

        return dp[m-1][n-1][1] % 1_000_000_007