class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        # dp[0][0] = 0
        # dp[i][0] = 0
        # dp[0][k] = 0
        for i in range(1, n+1):
            dp[i][1] = 1

        for i in range(1, n+1):
            for j in range(2, k+1):
                dp[i][j] += dp[i-1][j-1] + dp[i-1][j] * j
                dp[i][j] %= 1_000_000_007
        return dp[n][k]