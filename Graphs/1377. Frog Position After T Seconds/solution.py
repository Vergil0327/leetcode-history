class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set([1])
        def dfs(node, step):
            # count choices
            choices = []
            for nei in graph[node]:
                if nei in visited: continue
                visited.add(nei)
                choices.append(nei)
            prob = 1/len(choices) if choices else 0

            if node == target:
                if len(choices) == 0:
                    return 1 if step <= t else 0
                return 1 if step == t else 0

            res = 0
            for nei in choices:
                res = max(res, dfs(nei, step+1) * prob)
                
            return res

        return dfs(1, 0)
