class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([w, v])
            graph[v].append([w, u])

        pq = [[0, n]]
        distanceToLastNode = [inf]*(n+1)
        distanceToLastNode[n] = 0
        while pq:
            wei, node = heapq.heappop(pq)

            for w, nei in graph[node]:
                if (dist := distanceToLastNode[node]+w) < distanceToLastNode[nei]:
                    distanceToLastNode[nei] = dist
                    heapq.heappush(pq, [dist, nei])
        
        mod = 10**9 + 7

        @cache
        def dfs(node):
            if node == n: return 1
            res = 0
            for _, nei in graph[node]:
                if distanceToLastNode[nei] < distanceToLastNode[node]:
                    res = (res + dfs(nei))%mod
            return res
        return dfs(1)