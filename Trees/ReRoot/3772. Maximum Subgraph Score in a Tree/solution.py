"""
# Intuition

    parent_max
         |
        node
left_max     right_max

典型Re-root, 維護好`up`, `down`兩個方向的subgraph後, 計算最大值
"""

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(len(good)):
            if good[i] == 0:
                good[i] = -1

        
        down = [0] * n
        def dfs(node, prev):
            down[node] = good[node]
            for nxt in graph[node]:
                if nxt == prev: continue
                dfs(nxt, node)
                down[node] += max(0, down[nxt])
        dfs(0, -1)

        self.res = [0] * n
        upscore = [0] * n
        def reroot(node, prev):
            self.res[node] = down[node] + upscore[node]
            for nxt in graph[node]:
                if nxt == prev: continue
                remove = down[node] - max(0, down[nxt])
                upscore[nxt] = max(0, upscore[node] + remove)
                reroot(nxt, node)
        reroot(0, -1)
        return self.res
    