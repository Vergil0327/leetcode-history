class Solution:
    def numberOfSets(self, n: int, K: int) -> int:
        mod = 10**9 + 7

        # dp[i][k]: considering first i points, construct k line segments

        dp = [[[0]*2 for _ in range(K+1)]for _ in range(n)]
        presum = [[[0]*2 for _ in range(K+1)]for _ in range(n+1)]

        # base case
        for i in range(n):
            dp[i][0][0] = 1
            presum[i][0][0] = (presum[i-1][0][0] if i-1 >= 0 else 0) + dp[i][0][0]

            # dp[i][0][1] = 0 # 前i個點一定要用第i個點畫出0條線 -> 0
            # presum[i][0][1] = 0

        # dp[0][k][0] = 0
        # dp[0][k][1] = 0
        
        # dp[i][0], dp[0][i] 單獨處理
        for i in range(1, n):
            for k in range(1, min(i, K)+1):
                dp[i][k][0] = presum[i-1][k][1]
                dp[i][k][1] = presum[i-1][k-1][0] + presum[i-1][k-1][1]

                presum[i][k][1] = (presum[i-1][k][1] + dp[i][k][1])%mod
                presum[i][k-1][0] = (presum[i-1][k-1][0] + dp[i][k-1][0])%mod
                
        return (dp[n-1][K][0] + dp[n-1][K][1])%mod

class Solution2:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7

        # dp[i][k]: considering first i points, construct k line segments
        dp = [[0]*(k+1) for _ in range(n)]
        presum_dp = [[0]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
            presum_dp[i][0] = (presum_dp[i-1][0] if i-1>=0 else 0) + dp[i][0]

        for i in range(1, n):
            for kk in range(1, min(i, k)+1):
                dp[i][kk] = dp[i-1][kk]

                # for j in range(i-1, -1, -1):
                #     dp[i][kk] += dp[j][kk-1]
                dp[i][kk] += presum_dp[i-1][kk-1]
                
                dp[i][kk] %= mod

                presum_dp[i][kk] = (presum_dp[i-1][kk] + dp[i][kk]) % mod

        return dp[n-1][k]%mod
