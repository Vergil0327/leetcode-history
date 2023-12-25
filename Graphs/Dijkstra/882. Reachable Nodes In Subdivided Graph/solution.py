class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(lambda: defaultdict(int))
        for u, v, cnt in edges:
            graph[u][v] = cnt+1 # cnt + node-v self
            graph[v][u] = cnt+1 # cnt + node-u self
        
        dist = [0]*n
        visited = [0]*n
        pq = [[0, 0]]
        while pq:
            wei, node = heapq.heappop(pq)
            if visited[node]: continue
            visited[node] = 1
            dist[node] = wei

            for nei in graph[node]:
                if visited[nei]: continue
                if (newWei := wei + graph[node][nei]) <= maxMoves:
                    heapq.heappush(pq, [newWei, nei])

        res = 0
        for u, v, cnt in edges:
            count = 0
            if visited[u]:
                count += maxMoves - dist[u]
            if visited[v]:
                count += maxMoves - dist[v]
            res += min(cnt, count)

        for node in range(n):
            if visited[node]:
                res += 1
        return res