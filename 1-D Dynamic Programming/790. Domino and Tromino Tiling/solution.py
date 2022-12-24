class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1000000007
        # dp[i]: # of ways to tile 2 x i board
        dp = [0] * (n+1)
        
        # base case
        dp[0] = 1
        dp[1] = 1
        if n == 1: return 1
        dp[2] = 2
        if n == 2: return 2

        # dp[i] = dp[i-1] + dp[i-2] + 2 * (dp[i-3] + dp[i-4] + ... dp[0])
        presumDp = dp[1]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + 2*presumDp
            dp[i] %= MOD
            presumDp += dp[i-2]
        return dp[n]