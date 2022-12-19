# dest2wei[i] means minimum cost from src to i
#
# k stops means k+1 edges
# we can fly from src to dest step by step in k+1 times
# if `dest2wei[from]` is inf, it means we haven't reach `from` yet, we can't update its cost
# if `dest2wei[from]` not inf, we update it to minimum cost from src to dest
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dest2wei = defaultdict(lambda: inf)
        dest2wei[src] = 0

        while k+1 > 0:
            tmp = dest2wei.copy() # we can't read/update simultaneously
            for u, v, p in flights:
                if dest2wei[u] != inf:
                    tmp[v] = min(tmp[v], dest2wei[u] + p)
            dest2wei = tmp
            k -= 1

        return dest2wei[dst] if dest2wei[dst] != inf else -1
