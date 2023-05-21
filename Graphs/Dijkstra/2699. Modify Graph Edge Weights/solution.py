class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append([v,w])
            graph[v].append([u,w])

        def dijkstra(source, graph, skip_negative):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in graph[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    distance = d + w
                    if distance < dist[nei]:
                        dist[nei] = distance
                        parent[nei] = node
                        heappush(pq, [distance, nei])

            return dist, parent
        
        distReverse, _ = dijkstra(destination, graph, skip_negative=True)
        if distReverse[source] < target: return []

        dist, prev = dijkstra(source, graph, skip_negative=False)
        if dist[destination] > target: return []

        path = [destination]
        while path[-1] != source:
            path.append(prev[path[-1]])

        path = path[::-1] # shortest path

        weight = defaultdict(lambda: defaultdict(lambda: -1))
        for u,v,w in edges:
            weight[v][u] = weight[u][v] = w

        walked = 0
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            if weight[u][v] == -1:
                weight[v][u] = weight[u][v] = max(target-walked-distReverse[v], 1)
            walked += weight[u][v]

        for i in range(len(edges)):
            u,v = edges[i][0], edges[i][1]
            if weight[u][v] == -1:
                edges[i][2] = 2 * 10**9
            else:
                edges[i][2] = weight[u][v]
        
        return edges