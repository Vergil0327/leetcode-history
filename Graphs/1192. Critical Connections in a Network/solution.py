class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        dfn = [0] * n
        low = [0] * n
        parent = [-1] * n
        self.res = []
        self.timestamp = 0
        def dfs(node):
            visited[node] = True

            self.timestamp += 1
            dfn[node] = low[node] = self.timestamp

            for nei in graph[node]:
                if nei == parent[node]: continue

                if not visited[nei]:
                    parent[nei] = node
                    dfs(nei)

                    if low[nei] > dfn[node]: # critical edge
                        self.res.append([nei, node])

                    # if low[nei] >= dfn[node]: node is critical vertex

                    low[node] = min(low[node], low[nei])
                else:
                    low[node] = min(low[node], dfn[nei])

        for node in range(n):
            if not visited[node]:
                dfs(node)
        return self.res
