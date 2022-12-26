class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j]: the number of possible unique paths that robot can take to reach bottom-right
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 1:
                    dp[i][j] = 0
                    continue

                if i==1 and j==1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n]