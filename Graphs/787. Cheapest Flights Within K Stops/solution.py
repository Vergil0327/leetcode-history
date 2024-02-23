# dp[i] means the minimum cost from src to i
#
# k stops means k+1 edges
# we can fly from src to dest step by step in k+1 times
# if `dp[city]` is inf, it means we haven't reach `city` yet, we can't update its cost
# if `dp[city]` not inf, we update it to minimum cost from src to dest
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [inf]*n
        dp[src] = 0

        for _ in range(k+1):
            prev = dp.copy()
            for u, v, p in flights:
                dp[v] = min(dp[v], prev[u]+p)
        return dp[dst] if dp[dst] < inf else -1
