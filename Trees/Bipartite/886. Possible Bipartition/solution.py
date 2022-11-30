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