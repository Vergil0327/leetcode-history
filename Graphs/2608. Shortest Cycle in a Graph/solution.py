# DFS
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        self.res = inf
        def dfs(node, prev, size):
            cycle[node] = size
            for nei in graph[node]:
                if nei == prev: continue
                
                if cycle[nei] != -1:
                    if cycle[node] >= cycle[nei]:
                        self.res = min(self.res, cycle[node]+1-cycle[nei])
                    continue
                
                dfs(nei, node, size+1)
                
        for node in range(n):
            cycle = [-1] * n
            dfs(node, node, 0)
        return self.res if self.res != inf else -1
    
# BFS
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        self.res = inf
        for i in range(n):
            queue = deque([i])
            prev = list(range(n))
            size = [inf] * n
            size[i] = 0
            foundCycle = False
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for nei in graph[node]:
                        if prev[node] == nei: continue
                        if size[nei] != inf:
                            self.res = min(self.res, size[nei] + size[node] + 1)
                            foundCycle = True
                            break

                        prev[nei] = node
                        size[nei] = size[node]+1
                        queue.append(nei)
                    if foundCycle: break
                if foundCycle: break

        return self.res if self.res != inf else -1