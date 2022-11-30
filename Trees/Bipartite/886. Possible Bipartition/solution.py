class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list) # undirected graph
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        groups = [False] * (n+1) # labeled from 1 to n
        visited = set()
        def canGroup(node):
            for nei in graph[node]:
                if nei in visited: # check if `groups` is valid
                    if groups[nei] == groups[node]: return False
                    continue
                visited.add(nei)

                groups[nei] = not groups[node]
                if not canGroup(nei): return False
            return True

        for person in range(1, n+1):
            if person in visited: continue
            visited.add(person)

            if not canGroup(person): return False

        return True

# Union-Find
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            p = parent[node]
            while parent[p] != parent[parent[p]]:
                p = parent[p]
            return p

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2: return False

            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for node, neighbors in graph.items():
            nei = neighbors[0]
            
            p = find(nei)
            for other in neighbors[1:]:
                union(p, find(other))
            
                if find(node) == find(nei): return False
        return True