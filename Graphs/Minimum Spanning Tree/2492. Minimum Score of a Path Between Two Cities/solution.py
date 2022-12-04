# time: O(nlogn)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y): # union greater to smaller one to make parent be node1
            px, py = find(x), find(y)
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py
        
        roads.sort(key=lambda x:x[2])
        
        pathWeight = inf
        for u, v, w in roads:
            if find(u) != find(v):
                union(u, v)
                
        pathWeight = inf
        for u, v, w in roads:
            if find(u) == 1 or find(v) == 1: # exclude disconnected edges
                pathWeight = min(pathWeight, w) # find min score in connected components

        return pathWeight


# BFS - traverse whole connected components (SLOW)
# time: O(V+E)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append([v, w])
            graph[v].append([u, w])
            
        res = inf
        visited = set()
        queue = deque([[1, inf]])
        
        while queue:
            sz = len(queue)
            for _ in range(sz):
                node, score = queue.popleft()
                visited.add(node)
                res = min(res, score)
                
                for nei, wei in graph[node]:
                    if nei not in visited:
                        queue.append([nei, wei])
        return res
