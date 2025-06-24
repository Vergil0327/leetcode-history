class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        self.res = 0
        def dfs(node, parent):
            cur = cost[node]
            childs = []
            mx = 0
            for nxt in graph[node]:
                if nxt != parent:
                    x = dfs(nxt, node)
                    childs.append(x)
                    mx = max(mx, x)
            self.res += len(list(filter(lambda x: x != mx, childs)))
            return cur+mx
        dfs(0, -1)
        return self.res

            