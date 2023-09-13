# Intuition

可用dijkstra先求出minTime from 0 to n-1
再來對於`u -> v`來說, dp[v] += dp[u] where dp[v] means the number of ways to reach v in shortest time
這樣最終答案就是dp[n-1]

所以以一個Dijkstra框架來說:

cur -> nei
- if time+t < minTime[nei]: the first time to reach nei in shortest time => dp[nei] = dp[cur]
- if time+t == minTime[nei]: other ways to reach nei in shortest time => dp[nei] += dp[cur]

```py
minHeap = [[0, 0]] # time, node
visited = set()
while minHeap:
    time, cur = heapq.heappop(minHeap)
    if cur in visited: continue
    visited.add(cur)

    for t, nei in graph[cur]:
        if nei in visited: continue

        if time+t < minTime[nei]:
            minTime[nei] = time+t
            dp[nei] = dp[cur]
            heapq.heappush(minHeap, [time+t, nei])
        elif time+t == minTime[nei]:
            dp[nei] = (dp[nei] + dp[cur]) % 1_000_000_007
```