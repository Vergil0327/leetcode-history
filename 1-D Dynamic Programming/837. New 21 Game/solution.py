class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: return 1

        dp = [0] * (n+1)

        # base case
        dp[0] = 1
        presumDP = 1

        res = 0
        for i in range(1, n+1):
            dp[i] = presumDP/maxPts
            if i < k:
                presumDP += dp[i]
            else:
                res += dp[i]
            if i-maxPts >= 0:
                presumDP -= dp[i-maxPts]
        return res