class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        for u, v, t in edges:
            graph[u][v] = min(graph[u][v], t)
            graph[v][u] = min(graph[v][u], t)

        n = len(passingFees)

        pq = [[passingFees[0], 0, 0]] # cost, time, city
        cost = [inf]*n
        time = [inf]*n

        while pq:
            c0, t0, node = heapq.heappop(pq)
            if node == n-1: return c0

            for nei in graph[node]:
                c = c0 + passingFees[nei]
                t = t0 + graph[node][nei]
                if t > maxTime: continue
                if c < cost[nei]:
                    cost[nei] = c
                    time[nei] = t
                    heapq.heappush(pq, [c, t, nei])
                elif t < time[nei]:
                    time[nei] = t
                    heapq.heappush(pq, [c, t, nei])
        return -1
