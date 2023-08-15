class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(i):
            if i == 1: return 1
            if i == 2: return 2
            if i == 3: return 2

            res = i%2 + dfs(i//2)+1
            res = min(res, i%3 + dfs(i//3)+1)
            return res

        return dfs(n)
    
        # TLE
        # dp = [inf] * (n+1)
        # dp[n] = 0
        # for i in range(n, -1, -1):
        #     if i+1 <= n:
        #         dp[i] = min(dp[i], dp[i+1]+1)
        #     if i%2 == 0:
        #         dp[i//2] = min(dp[i//2], dp[i]+1)
        #     if i%3 == 0:
        #         dp[i//3] = min(dp[i//3], dp[i]+1)

        # return dp[0]
