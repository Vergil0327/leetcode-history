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
# dp[n]: minimum # of perfect squares which sum to n by using perfs[:i]
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf]*(n+1) # maximum # of perfect squares that can sum up to n is n. (1+1+...+1 to n)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(sqrt(n))+1):
                square = j**2
                if i-square >= 0:
                    dp[i] = min(dp[i], dp[i-square]+1)
                else:
                    break
        return dp[n]