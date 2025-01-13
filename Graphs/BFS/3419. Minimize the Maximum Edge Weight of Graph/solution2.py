class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        path = [[] for _ in range(n)]
        for u, v, w in edges:
            path[v].append((u, w))
        
        # dijkstra
        dis = [inf] * n
        dis[0] = 0
        
        hpq = [(0, 0)]
        while hpq:
            d, u = heappop(hpq)
            if dis[u] == d:
                for v, w in path[u]:
                    nd = max(d, w)
                    if nd < dis[v]:
                        dis[v] = nd
                        heappush(hpq, (nd, v))
        
        res = max(dis)
        return res if res < inf else -1