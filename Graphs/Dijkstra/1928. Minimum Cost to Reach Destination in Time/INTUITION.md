# Intuition

minimum cost => try BFS
build adjacency list graph[u][v] = min(t1, t2, ...)

0 -> n-1, find minimum cost from those path to destination within maxTime

cost低的有可能超時, 所以重點在於如何去除會超時的可能路徑
並且:
1. 在不超出maxTime情況下, 如果cost更低, 選cost更低的
2. 在不超出maxTime情況下, 如果cost一樣, 選時間更低的

所以我們必須紀錄抵達city時的time跟cost
我們紀錄dp[city][time] = cost, 然後cost越低越好

最後我們就能在範圍[0, maxTime]遍歷`t`, 從dp[n-1][t]中找出最小cost

```py
graph = defaultdict(lambda: defaultdict(lambda: inf))
for u, v, t in edges:
    graph[u][v] = min(graph[u][v], t)
    graph[v][u] = min(graph[v][u], t)

n = len(passingFees)
queue = deque([(passingFees[0], 0, 0)]) # cost, time, city
dp = [defaultdict(lambda: inf) for _ in range(n)]
while queue:
    for _ in range(len(queue)):
        c, t, node = queue.popleft()
        if c > dp[node][t]: continue
        dp[node][t] = c

        for nei in graph[node]:
            time = t + graph[node][nei]
            if time > maxTime: continue

            cost = c + passingFees[nei]
            if cost > dp[nei][time]: continue
            queue.append([cost, time, nei])

res = inf
for t in range(maxTime+1):
    res = min(res, dp[n-1][t])
return res if res < inf else -1
```

**可惜最終TLE**

要比BFS更快, 那可能得往 dijkstra 去想了
如同前面BFS所述, 我們勢必得紀錄抵達每個city時的cost跟time
我們分別用`cost[city]`跟`time[city]`紀錄抵達city時的最小cost以及相對應時間
那麼框架如下:

```py
pq = [[passingFees[0], 0, 0]] # cost, time, city
cost = [inf]*n
time = [inf]*n
res = inf
while pq:
    c0, t0, node = heapq.heappop(pq)
    if node == n-1: return c0

    for nei in graph[node]:
        c = c0 + passingFees[nei]
        t = t0 + graph[node][nei]
        if t > maxTime: continue
        
        # TODO: prune branches
        heapq.heappush(pq, [c, t, nei])
return -1
````

最終重點還是在於如何去除那些較差的路徑選擇

如同一開始所想, 有cost更低的, 那肯定選更低的
在所有合法 <= maxTime 的選擇中, 我們沒必要去嘗試那些cost更高的情況, 所以:

```py
if c < cost[nei]:
    cost[nei] = c
    time[nei] = t
    heapq.heappush(pq, [c, t, nei])
```
並同時更新cost[nei]跟time[nei]

那如果沒有cost更低的路徑了呢?, 那就是再從 c >= cost[nei]的這些選擇中選最有潛力的, 也就是時間花費最少的
```py
elif t < time[nei]:
    time[nei] = t
    heapq.heappush(pq, [c, t, nei])
```

而這時我們記得更新time[nei] = t, 在這之後就沒有必要嘗試那些時間花費更多的路徑選擇了

所以藉由:
```py
if c < cost[nei]:
    cost[nei] = c
    time[nei] = t
    heapq.heappush(pq, [c, t, nei])
elif t < time[nei]:
    time[nei] = t
    heapq.heappush(pq, [c, t, nei])
```
我們能持續嘗試那些cost較低的路徑, 以及那些cost較高但時間花費較低的路徑
如果最終都找不到, 那就返回`-1`, 代表我們無法在maxTime時間內抵達終點