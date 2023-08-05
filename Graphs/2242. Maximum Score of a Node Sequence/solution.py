class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            heapq.heappush(graph[u], [scores[v], v])
            if len(graph[u]) > 3:
                heapq.heappop(graph[u])
            heapq.heappush(graph[v], [scores[u], u])
            if len(graph[v]) > 3:
                heapq.heappop(graph[v])

        res = -1
        for u, v in edges:
            score = scores[u] + scores[v]
            for scoreA, a in graph[u]:
                if a == u or a == v: continue
                for scoreB, b in graph[v]:
                    if b == a or b == u or b == v: continue
                    res = max(res, score+scoreA+scoreB)
        return res