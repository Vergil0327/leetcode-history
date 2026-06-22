class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        graph = [[]*n for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        inf = float('inf')
        def dfs(node, prev):
            finish = baseTime[node]
            mn, mx = inf, -inf
            for nxt in graph[node]:
                if nxt == prev: continue
                
                task = dfs(nxt, node)
                mn = min(mn, task)
                mx = max(mx, task)
            ownDuration = finish + ((mx-mn) if mx-mn > 0 else 0)
            latest = (mx if mx > -inf else 0)
            return ownDuration + latest
        return dfs(0, -1)