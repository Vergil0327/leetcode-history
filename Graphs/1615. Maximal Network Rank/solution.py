class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indeg = [0] * n
        graph = defaultdict(set)

        for a, b in roads:
            indeg[a] += 1
            indeg[b] += 1
            graph[a].add(b)
            graph[b].add(a)

        res = 0
        for a in range(n):
            for b in range(n):
                if a == b: continue

                res = max(res, indeg[a]+indeg[b] - (1 if a in graph[b] else 0))
        return res