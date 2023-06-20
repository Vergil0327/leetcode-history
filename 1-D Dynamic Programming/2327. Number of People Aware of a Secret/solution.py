class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9+7
        dp = [0] * (n+1)
        dp[1] = 1
        for day in range(1, n+1):
            start, end = day+delay, min(n+1, day+forget)
            for i in range(start, end):
                dp[i] += dp[day]

            if day-forget >= 0:
                dp[day-forget] = 0 # forget
        return sum(dp)%mod
    
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9+7

        dp = [0] * (n+1)
        diff = [0] * (n+1)

        # base case
        diff[1] += 1
        diff[2] -= 1

        for i in range(1, n+1):
            dp[i] = dp[i-1] + diff[i]

            if i+delay <= n:
                diff[i+delay] += dp[i]
            if i+forget <= n:
                diff[i+forget] -= dp[i]

            if i-forget >= 0:
                dp[i-forget] = 0 # forget

        return sum(dp)%mod