from collections import defaultdict
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(lambda: defaultdict(int))
        for u, v, w in edges:
            graph[u][v] = w

        @lru_cache(None)
        def dfs(node, edge):
            if edge == k:
                return [0], True

            res = set()
            state = False
            for nxt in graph[node]:
                arr, valid = dfs(nxt, edge+1)
                if valid:
                    state = True
                    for x in arr:
                        if x+graph[node][nxt] < t:
                            res.add(x+graph[node][nxt])

            return res, state
        
        res = -1
        for node in range(n):
            ans, valid = dfs(node, 0)
            if valid and ans:
                res = max(res, max(ans))
        return res