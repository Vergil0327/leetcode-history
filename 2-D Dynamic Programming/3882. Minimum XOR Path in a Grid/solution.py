class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[row][col][xor_state] = valid or not
        dp = [[[0 for k in range(1024)] for j in range(n)] for i in range(m)]
        dp[0][0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                for k in range(1024):
                    xk = k ^ grid[i][j]
                    if i and dp[i - 1][j][xk]:
                        dp[i][j][k] = True
                    if j and dp[i][j - 1][xk]:
                        dp[i][j][k] = True

        for state in range(1024):
            if dp[m-1][n-1][state]: return state
            