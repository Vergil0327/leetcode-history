# Top-Dwon: O(n*sqrt(n)), maximum # of for-loop would be sqrt(n)
class Solution:
    def numSquares(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n):
            if n == 0: return 0
            if n < 0: return inf

            cnt = n
            for i in range(1, n+1):
                perf = i**2
                if perf > n: break
                cnt = min(cnt, dfs(n-perf) + 1)
            return cnt
        return dfs(n)

# Bottom-UP
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[n]: minimum # of perfect squares which sum to n by using perfs[:i]
        dp = [n] * (n+1) # maximum # of perfect squares that can sum up to n is n. (1+1+...+1 to n)
        dp[0] = 0
        for total in range(1, n+1):
            for j in range(1, n+1):
                perf = j ** 2
                if perf > n: break
                dp[total] = min(dp[total], dp[total-perf] + 1)
        return dp[n]

