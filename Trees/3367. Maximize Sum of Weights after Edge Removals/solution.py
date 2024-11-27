class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        graph = defaultdict(lambda: defaultdict(int))
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        def dfs(node, prev):
            res = 0

            diff = []
            for nxt in graph[node]:
                if nxt == prev: continue

                sum1, sum2 = dfs(nxt, node)
                res += sum2
                diff.append(max(0, sum1+graph[node][nxt] - sum2))
            
            diff.sort(reverse=True)
            
            return res + sum(diff[:k-1]), res + sum(diff[:k])
        return dfs(0, -1)[1]
