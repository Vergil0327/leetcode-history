# DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        bipartite = [False] * len(graph)
        visited = set()
        def dfs(node):
            for nei in graph[node]:
                if nei in visited:
                    if bipartite[nei] == bipartite[node]: return False
                    continue
                visited.add(nei)

                bipartite[nei] = not bipartite[node]
                if not dfs(nei): return False
            return True

        for node, _ in enumerate(graph):
            if node in visited: continue
            visited.add(node)

            if not dfs(node): return False
        return True
    
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n
        
        def dfs(node, tag):
            visited[node] = tag
            for nei in graph[node]:
                if visited[nei] != -1:
                    if visited[nei] == tag: return False
                    continue

                visited[nei] = 1-tag
                if not dfs(nei, visited[nei]): return False
            return True

        for node in range(n):
            if visited[node] == -1:
                if not dfs(node, 0): return False

        return True