class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = int(1e9+7)

        dp = [[0] * (k+1)for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, k+1):
                # for m in range(0, min(j, i-1)+1):
                #     if j-m < 0: continue
                #     dp[i][j] += dp[i-1][j-m]
                #     dp[i][j] %= MOD
                dp[i][j] = dp[i][j-1] + dp[i-1][j-0] - (dp[i-1][j-i] if j-i >= 0 else 0)
                dp[i][j] %= MOD

        return dp[n][k]