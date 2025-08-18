from collections import defaultdict
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v,w])
            graph[v].append([u,2*w]) # reversed

        min_heap = [[0, 0]] # cost, node
        visited = [0] * n
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node == n-1: return cost
            if visited[node]: continue
            visited[node] = 1

            for nxt, wei in graph[node]:
                heapq.heappush(min_heap, [cost+wei, nxt])
        return -1