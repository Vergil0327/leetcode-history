
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7

        @cache
        def dfs(zero, one, last):
            if zero == 0 and one == 0: return 1

            res = 0
            if last == 0:
                for consecutiveOne in range(1, limit+1):
                    if consecutiveOne <= one:
                        res += dfs(zero, one-consecutiveOne, 1)
            else:
                for consecutiveZero in range(1, limit+1):
                    if consecutiveZero <= zero:
                        res += dfs(zero-consecutiveZero, one, 0)
            return res%mod

        return (dfs(zero, one, 0) + dfs(zero, one, 1))%mod


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(one+1):
            if i <= limit:
                dp[0][i][0] = 1
                
        for i in range(zero+1):
            if i <= limit:
                dp[i][0][1] = 1
                
        for x in range(1, zero+1):
            for y in range(1, one+1):
                dp[x][y][0] += sum(dp[x][y-consecutive][1] for consecutive in range(1, min(y, limit)+1))
                dp[x][y][0] %= mod

                dp[x][y][1] += sum(dp[x-consecutive][y][0] for consecutive in range(1, min(x, limit)+1))
                dp[x][y][1] %= mod
        return (dp[zero][one][0] + dp[zero][one][1])%mod