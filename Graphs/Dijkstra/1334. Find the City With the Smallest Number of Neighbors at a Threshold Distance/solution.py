# Dijkstra with priority queue
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def dijkstra(pq, weight):
            while pq:
                for _ in range(len(pq)):
                    w, node = heapq.heappop(pq)
                    for nei, wei in graph[node]:
                        if w+wei < weight[nei]:
                            weight[nei] = w + wei
                            heapq.heappush(pq, [weight[nei], nei])

        weights = [[inf]*n for _ in range(n)]
        for node in range(n):
            weights[node][node] = 0
            pq = [[0, node]]
            dijkstra(pq, weights[node])

        minNeighborCiy = -1
        minNeighbor = inf
        for node in range(n):
            countCanReach = 0
            
            for city, wei in enumerate(weights[node]):
                if city == node: continue
                if wei > threshold: continue
                countCanReach += 1
            
            if countCanReach < minNeighbor:
                minNeighbor = countCanReach
                minNeighborCiy = node
            elif countCanReach == minNeighbor:
                minNeighborCiy = max(minNeighborCiy, node)
            
        return minNeighborCiy

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def bfs(queue, weight):
            while queue:
                for _ in range(len(queue)):
                    node, w = queue.popleft()
                    for nei, wei in graph[node]:
                        if w+wei < weight[nei]:
                            weight[nei] = w + wei
                            queue.append([nei, weight[nei]])
            
        weights = [[inf]*n for _ in range(n)]
        for node in range(n):
            weights[node][node] = 0
            queue = deque([[node, 0]])
            bfs(queue, weights[node])
        
        minNeighborCiy = -1
        minNeighbor = inf
        for node in range(n):
            countCanReach = 0
            
            for city, wei in enumerate(weights[node]):
                if city == node: continue
                if wei > threshold: continue
                countCanReach += 1
            
            if countCanReach < minNeighbor:
                minNeighbor = countCanReach
                minNeighborCiy = node
            elif countCanReach == minNeighbor:
                minNeighborCiy = max(minNeighborCiy, node)
            
        return minNeighborCiy

# Bellman-Ford - TLE
class Solution_TLE:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def bellmenFord(edges, weight):
            for _ in range(len(edges)-1):
                tmp = weight.copy()
                for u, v, w in edges:
                    if weight[u] != inf:
                        tmp[v] = min(tmp[v], weight[u]+w)
                weight[:] = tmp[:]

        weights = [[inf]*n for _ in range(n)]
        for node in range(n):
            weights[node][node] = 0 # starting point, weight of node to itself is 0
            bellmenFord(edges, weights[node])

        minNeighborCiy = -1
        minNeighbor = inf
        for node in range(n):
            countCanReach = 0
            
            for city, wei in enumerate(weights[node]):
                if city == node: continue
                if wei > threshold: continue
                countCanReach += 1
            
            if countCanReach < minNeighbor:
                minNeighbor = countCanReach
                minNeighborCiy = node
            elif countCanReach == minNeighbor:
                minNeighborCiy = max(minNeighborCiy, node)
            
        return minNeighborCiy

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        def bellmenFord(edges, weight):
            for _ in range(len(edges)-1):
                tmp = weight.copy()
                for u, v, w in edges:
                    if weight[u] != inf:
                        tmp[v] = min(tmp[v], weight[u]+w)
                    
                    # bi-directional
                    if weight[v] != inf:
                        tmp[u] = min(tmp[u], weight[v]+w)
                weight[:] = tmp[:]

        weights = [[inf]*n for _ in range(n)]
        for node in range(n):
            weights[node][node] = 0 # weights[node][node] = 0 # starting point, weight of node to itself is 0
            bellmenFord(edges, weights[node])

        minNeighborCiy = -1
        minNeighbor = inf
        for node in range(n):
            countCanReach = 0
            for city, wei in enumerate(weights[node]):
                if city == node: continue
                if wei > threshold: continue
                countCanReach += 1
            
            if countCanReach < minNeighbor:
                minNeighbor = countCanReach
                minNeighborCiy = node
            elif countCanReach == minNeighbor:
                minNeighborCiy = max(minNeighborCiy, node)
            
        return minNeighborCiy

# Floyd–Warshall
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        distance = [[inf] * n for _ in range(n)]
        for u, v, w in edges:
            distance[u][v] = w
            distance[v][u] = w
        for city in range(n):
            distance[city][city] = 0
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
        
        minNeighborCity = -1
        minNeighbor = inf
        for city in range(n):
            total = sum(1 for dist in distance[city] if dist <= threshold)
            if total < minNeighbor:
                minNeighbor = total
                minNeighborCity = city
            elif total == minNeighbor:
                minNeighborCity = max(minNeighborCity, city)
        return minNeighborCity
