class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        for u, v, w in edges:
            graph[u][v] = min(graph[u][v], w)
        
        def dijkstra(graph, u):
            dp = [inf]*n
            dp[u] = 0

            pq = [[0, u]]
            while pq:
                w, cur = heapq.heappop(pq)

                for nxt in graph[cur]:
                    if w+graph[cur][nxt] < dp[nxt]:
                        dp[nxt] = w+graph[cur][nxt]
                        heapq.heappush(pq, [dp[nxt], nxt])
            return dp

        dp1 = dijkstra(graph, src1) # dp1[node]: the minimum weigh of path from src1 to any other node
        dp2 = dijkstra(graph, src2) # dp1[node]: the minimum weigh of path from src2 to any other node

        graphRev = defaultdict(lambda: defaultdict(lambda: inf))
        for u, v, w in edges:
            graphRev[v][u] = min(graphRev[v][u], w)
        dp3 = dijkstra(graphRev, dest)

        res = min(dp1[commonNode] + dp2[commonNode] + dp3[commonNode] for commonNode in range(n))
        return res if res < inf else -1