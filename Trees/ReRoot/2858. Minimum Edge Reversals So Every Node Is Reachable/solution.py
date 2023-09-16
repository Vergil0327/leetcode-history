class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append([0, v])
            graph[v].append([1, u])
            
        @cache
        def dfs(node, prev):
            res = 0
            for cost, nei in graph[node]:
                if nei == prev: continue
                res += dfs(nei, node) + cost
            return res
        
        res = []
        for i in range(n):
            res.append(dfs(i, -1))
        return res

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append([0, v])
            graph[v].append([1, u])

        def dfs(node, prev):
            res = 0
            for cost, nei in graph[node]:
                if nei == prev: continue
                res += dfs(nei, node) + cost
            return res

        res = [-1] * n
        res[0] = dfs(0, -1)

        def reroot(node, cost = 0):
            res[node] = cost
            for c, nei in graph[node]:
                if res[nei] < 0:
                    # node -> nei: c
                    # nei -> node: 1-c
                    reroot(nei, cost - c + (1-c))
        reroot(0, res[0])
        return res