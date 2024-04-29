class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = dp[0][0][1] = 1
        for i in range(1, one+1):
            if i <= limit:
                dp[0][i][0] = 1
                
        for i in range(1, zero+1):
            if i <= limit:
                dp[i][0][1] = 1

        presum_dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(one+1):
            presum_dp[0][i][0] = dp[0][i][0]
        for i in range(zero+1):
            presum_dp[i][0][1] = dp[i][0][1]

        for x in range(1, zero+1):
            for y in range(1, one+1):
                # for consecutive in range(1, min(y, limit)+1):
                #     dp[x][y][0] += dp[x][y-consecutive][1]
                #     dp[x][y][0] %= mod
                dp[x][y][0] = presum_dp[x][y-1][1] - (presum_dp[x][y-limit-1][1] if y-limit-1 >= 0 else 0)
                dp[x][y][0] = (dp[x][y][0] + mod) % mod

                # for consecutive in range(1, min(x, limit)+1):
                #     dp[x][y][1] += dp[x-consecutive][y][0]
                #     dp[x][y][1] %= mod
                dp[x][y][1] = presum_dp[x-1][y][0] - (presum_dp[x-limit-1][y][0] if x-limit-1 >= 0 else 0)
                dp[x][y][1] = (dp[x][y][1] + mod) % mod

                presum_dp[x][y][0] = (presum_dp[x-1][y][0] + dp[x][y][0]) % mod
                presum_dp[x][y][1] = (presum_dp[x][y-1][1] + dp[x][y][1]) % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod