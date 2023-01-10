# Top-Down
class Solution:
    def integerReplacement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n):
            if n == 1: return 0

            if n&1 == 0:
                return dfs(n//2) + 1
            else:
                return min(dfs(n+1), dfs(n-1)) + 1
        return dfs(n)

# Bottom-Up
class Solution:
    def integerReplacement(self, n: int) -> int:
        dp = [inf] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]+1
            else:
                # dp[i] = min(dp[i-1], dp[i+1])+1
                # dp[i+1] = 1 + dp[(i+1)//2]+1
                dp[i] = min(dp[i-1], dp[(i+1)//2]+1)+1
        return dp[n]