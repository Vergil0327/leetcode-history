class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        orient = defaultdict(int)
        for u, v in connections:
            orient[(u,v)] = 1
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        def dfs(node, prev):
            for nei in graph[node]:
                if nei == prev: continue
                self.res += orient[(node, nei)]
                dfs(nei, node)
        dfs(0, 0)
        return self.res