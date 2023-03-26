# Concise Version - Topological Sort by DFS
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
            
        dist = [0] * n
        visited = [False] * n
        cycle = [False] * n
        res = -1

        def dfs(node, step):
            nonlocal res

            if node != -1:
                if not visited[node]:
                    visited[node] = True
                    dist[node] = step

                    cycle[node] = True
                    dfs(edges[node], step+1)
                    cycle[node] = False
                elif cycle[node] :
                    res = max(res, step-dist[node])

        for node in range(n):
            if visited[node]: continue
            dfs(node, 0)
        return res
    
# Topological Sort in BFS
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in enumerate(edges):
            if v == -1: continue
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([node for node, indeg in enumerate(indegree) if indeg == 0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                edges[node] = -1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in enumerate(edges):
            if v == -1: continue
            pu, pv = find(u), find(v)
            if pu == pv: continue
            if rank[pu] <= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
        mx = max(rank)
        return mx if mx != 1 else -1

# first try - only beats 5 %
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        visited = [False] * n
        res = -1
        def dfs(node, step, distance):
            nonlocal res
            while edges[node] != -1:
                if distance[node] != -1:
                    res = max(res, step - distance[node])
                    break
                
                if visited[node]: break
                visited[node] = True

                distance[node] = step
                step += 1
                node = edges[node]
        
        # if indegree[i] == 0, it can't be part of cycle
        indegrees = [False] * n
        for node in edges:
            if node == -1: continue
            indegrees[node] = True

        for node in range(n):
            if visited[node]: continue # skip connected component we've already explore. 1 outdegree at most, each node only can be 1 part of cycle
            if not indegrees[node]: continue
            if edges[node] == -1: continue # if it doesn't connect to node, it can't be cycle
            if n-node <= res: break # even rest of node form a cycle, size is still less than res
            dfs(node, 0, [-1] * n)
        
        return res