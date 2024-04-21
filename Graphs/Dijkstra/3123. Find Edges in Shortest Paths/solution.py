class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = defaultdict(lambda: defaultdict(int))
        for i, (u, v, w) in enumerate(edges):
            graph[u][v] = w
            graph[v][u] = w
            
        def dijkstra(src, dst):
            cost = [inf]*n
            cost[src] = 0
            
            pq = [(0,src)]
            seen = set()
            while pq:
                wei, node = heapq.heappop(pq)
                if node in seen: continue
                seen.add(node)
                cost[node] = wei

                for nxt in graph[node]:
                    if wei+graph[node][nxt] < cost[nxt]:
                        heapq.heappush(pq, [wei+graph[node][nxt], nxt])
            return cost

        costFromSrc = dijkstra(0, n-1)
        costFromDst = dijkstra(n-1, 0)

        minCost = costFromSrc[n-1]
        res = [False]*len(edges)
        if minCost == inf: return res

        for i, (u,v,w) in enumerate(edges):
            isShortedpath = costFromSrc[u] + w + costFromDst[v] == minCost or costFromSrc[v] + w + costFromDst[u] == minCost
            if isShortedpath:
                res[i] = True
        return res
