# Top-Down DP - Memory Limit Exceeded
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9+7)
        
        @lru_cache(None)
        def dfs(i, absent, trailingL):
            if i == n: return 1
            
            res = dfs(i+1, absent, 0)
            if absent < 1:
                res += dfs(i+1, absent+1, 0)
                res %= MOD
            if trailingL < 2:
                res += dfs(i+1, absent, trailingL+1)
                res %= MOD

            res %= MOD
            return res

        return dfs(0, 0, 0)

# Bottom-Up
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9+7)
        A = L = P = 1

        # dp[i][absent][trailingLate]
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]
        dp[0][0][0] = 1 # only 1 possibility when length = 1 and no absent and not trailing late
        dp[0][0][1] = 0
        dp[0][0][2] = 0
        dp[0][1][0] = 0
        dp[0][1][1] = 0
        dp[0][1][2] = 0

        for i in range(1, n+1):
            dp[i][0][0] = dp[i-1][0][0]*P + dp[i-1][0][1]*P + dp[i-1][0][2]*P
            dp[i][0][0] %= MOD
            dp[i][0][1] = dp[i-1][0][0]*L # append Late to dp with 0 trailling L
            dp[i][0][1] %= MOD
            dp[i][0][2] = dp[i-1][0][1]*L # append Late to dp with 1 trailing L
            dp[i][0][2] %= MOD
            dp[i][1][0] = dp[i-1][0][0]*A + dp[i-1][0][1]*A + dp[i-1][0][2]*A + dp[i-1][1][0]*P + dp[i-1][1][1]*P + dp[i-1][1][2]*P
            dp[i][1][0] %= MOD
            dp[i][1][1] = dp[i-1][1][0]*L # append Late to dp with 0 trailling L
            dp[i][1][1] %= MOD
            dp[i][1][2] = dp[i-1][1][1]*L # append Late to dp with 1 trailing L
            dp[i][1][2] %= MOD
        
        return (dp[n][0][0]+dp[n][0][1]+dp[n][0][2]+dp[n][1][0]+dp[n][1][1]+dp[n][1][2])%MOD

# Space-Optimized
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9+7)

        # dp[i][absent][trailingLate]
        # dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]
        dp00 = [0]*(n+1)
        dp01 = [0]*(n+1)
        dp02 = [0]*(n+1)
        dp10 = [0]*(n+1)
        dp11 = [0]*(n+1)
        dp12 = [0]*(n+1)
        # dp[0][0][0] = 1
        dp00[0] = 1
        # dp[0][0][1] = 0
        dp01[0] = 0
        # dp[0][0][2] = 0
        dp02[0] = 0
        # dp[0][1][0] = 0
        dp10[0] = 0
        # dp[0][1][1] = 0
        dp11[0] = 0
        # dp[0][1][2] = 0
        dp12[0] = 0

        for i in range(1, n+1):
            dp00[i] = dp00[i-1] + dp01[i-1] + dp02[i-1]
            dp00[i] %= MOD
            dp01[i] = dp00[i-1]
            dp01[i] %= MOD
            dp02[i] = dp01[i-1]
            dp02[i] %= MOD
            dp10[i] = dp00[i-1] + dp01[i-1] + dp02[i-1] + dp10[i-1] + dp11[i-1] + dp12[i-1]
            dp10[i] %= MOD
            dp11[i] = dp10[i-1]
            dp11[i] %= MOD
            dp12[i] = dp11[i-1]
            dp12[i] %= MOD
        
        return (dp00[n]+dp01[n]+dp02[n]+dp10[n]+dp11[n]+dp12[n])%MOD

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = int(1e9+7)
        A = L = P = 1

        # dp[i][absent][trailingLate]
        # dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]
        # dp[0][0][0] = 1
        # dp[0][0][1] = 0
        # dp[0][0][2] = 0
        # dp[0][1][0] = 0
        # dp[0][1][1] = 0
        # dp[0][1][2] = 0

        # dp00 = [0]*(n+1)
        # dp01 = [0]*(n+1)
        # dp02 = [0]*(n+1)
        # dp10 = [0]*(n+1)
        # dp11 = [0]*(n+1)
        # dp12 = [0]*(n+1)
        # dp00[0] = 1
        # dp01[0] = 0
        # dp02[0] = 0
        # dp10[0] = 0
        # dp11[0] = 0
        # dp12[0] = 0

        prevdp = [0] * 6
        dp = [0] * 6
        prevdp[0] = 1

        for i in range(1, n+1):
            # dp00[i] = dp00[i-1] + dp01[i-1] + dp02[i-1]
            dp[0] = prevdp[0] + prevdp[1] + prevdp[2]
            dp[0] %= MOD
            # dp01[i] = dp00[i-1]
            dp[1] = prevdp[0]
            dp[1] %= MOD
            # dp02[i] = dp01[i-1]
            dp[2] = prevdp[1]
            dp[2] %= MOD
            # dp10[i] = dp00[i-1] + dp01[i-1] + dp02[i-1] + dp10[i-1] + dp11[i-1] + dp12[i-1]
            dp[3] = prevdp[0] + prevdp[1] + prevdp[2] + prevdp[3] + prevdp[4] + prevdp[5]
            dp[3] %= MOD
            # dp11[i] = dp10[i-1]
            dp[4] = prevdp[3]
            dp[4] %= MOD
            # dp12[i] = dp11[i-1]
            dp[5] = prevdp[4]
            dp[5] %= MOD

            dp, prevdp = prevdp, dp
        
        return sum(prevdp)%MOD