class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t])

        minH = [[0, k]]
        time = 0
        visited = set()
        while minH:
            t, curr = heapq.heappop(minH)
            if curr in visited: continue
            time = max(time, t)

            visited.add(curr)
            for nei, weight in graph[curr]:
                heapq.heappush(minH, [t+weight, nei])
        return time if len(visited) == n else -1
