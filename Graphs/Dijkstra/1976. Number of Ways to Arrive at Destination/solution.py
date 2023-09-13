class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([time, v])
            graph[v].append([time, u])

        minTime = [inf] * n
        minTime[0] = 0

        dp = [0] * n
        dp[0] = 1

        # dijkstra
        minHeap = [[0, 0]] # time, node
        visited = set()
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited: continue
            visited.add(node)

            for t, nei in graph[node]:
                if nei in visited: continue

                if time+t < minTime[nei]:
                    minTime[nei] = time+t
                    dp[nei] = dp[node]
                    heapq.heappush(minHeap, [time+t, nei])
                elif time+t == minTime[nei]:
                    dp[nei] = (dp[nei] + dp[node]) % 1_000_000_007

        return dp[n-1]
