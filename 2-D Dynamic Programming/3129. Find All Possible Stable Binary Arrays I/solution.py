
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
