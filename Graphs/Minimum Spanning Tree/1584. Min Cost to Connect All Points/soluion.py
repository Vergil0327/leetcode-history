# O(n^2 * logn)
# Prim's algorithm: BFS + hashset & min heap
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

        n = len(points)
        adjList = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    adjList[i].append([dist(points[i], points[j]), j])
        
        cost = 0
        minH = [[0, 0]] # [cost, point_i]
        visited = set()
        while len(visited) < n:
            c, idx = heapq.heappop(minH)
            if idx not in visited:
                cost += c
                visited.add(idx)
                
                for neiCost, nei in adjList[idx]:
                    if nei not in visited:
                        heapq.heappush(minH, [neiCost, nei])
        return cost

# Kruskal: O(ElogE), E means # of edges
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

        n = len(points)

        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py

        edges = [] # [distance, start, end]
        for i in range(n):
            for j in range(i+1, n):
                edges.append([dist(points[i], points[j]), i, j])

        edges.sort()
        numEdges = 0 # n-1 edges for n nodes
        cost = 0
        for dist, src, dst in edges:
            if find(src) != find(dst):
                union(src, dst)
                numEdges += 1
                cost += dist
            if numEdges == n-1: break
        return cost