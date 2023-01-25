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