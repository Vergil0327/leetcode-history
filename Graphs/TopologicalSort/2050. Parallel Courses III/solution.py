class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in relations:
            u, v = u-1, v-1
            graph[u].append(v)
            indeg[v] += 1

        pq = [[time[node], node] for node, deg in enumerate(indeg) if deg == 0]
        heapq.heapify(pq)
        
        res = -inf
        while pq:
            wei, node = heapq.heappop(pq)
            res = max(res, wei)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    heapq.heappush(pq, [wei+time[nei], nei])
            
        return res
