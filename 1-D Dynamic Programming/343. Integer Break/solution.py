# Top-Down DP
class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n):
            res = 0
            for num in range(1, n):
                res = max(res, num * (n-num))
                res = max(res, num * dfs(n-num))
            return res
        return dfs(n)

# Bottom-UP
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for num in range(1, n+1):
            for i in range(1, num):
                dp[num] = max(dp[num], i * (num-i), i * dp[num-i])

        return dp[n]