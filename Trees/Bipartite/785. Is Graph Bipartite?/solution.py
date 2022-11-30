# DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A, B = set(), set()
        visited = set()
        def dfs(node):
            if node in visited: return True
            visited.add(node)

            if node not in A and node not in B:
                A.add(node)

            for nei in graph[node]:
                if node in A:
                    if nei in A: return False
                    B.add(nei)
                else:
                    if nei in B: return False
                    A.add(nei)
                if not dfs(nei): return False
            return True

        for node, _ in enumerate(graph):
            if not dfs(node): return False
        return True

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