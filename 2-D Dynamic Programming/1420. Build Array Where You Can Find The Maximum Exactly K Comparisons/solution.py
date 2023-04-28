class Solution:
    def numOfArrays(self, n: int, m: int, K: int) -> int:
        mod = 10**9+7

        dp = [[[0]*(K+1) for _ in range(m+1)] for _ in range(n)]

        for mx in range(1, m+1):
            dp[0][mx][1] = 1

        for i in range(1, n):
            for mx in range(1, m+1):
                for k in range(1, min(i+1, K)+1):
                    for curr in range(1, mx):
                        dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][curr][k-1])%mod
                    dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][mx][k] * mx)%mod
                    
        res = 0
        for mx in range(1, m+1):
            res = (res + dp[n-1][mx][K])%mod
        return res
