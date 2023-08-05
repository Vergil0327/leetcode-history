# Intuition

iterate edges [u, v], and iterate neighborNode1 in graph[u] and neighborNode2 in graph[v].
if all these 4 nodes are unique, we find valid sequence of length = 4.

then our problem reduces to how to remove other two useless or duplicate node

since each node only connect to 3 nodes at most for 4-node sequece, we can build our adjacency list `graph` and only store 3 nodes with top-3 score

thus, we can use min heap with size=3 to store graph[node] = min_heap where min_heap store `[score, neighbor]` (score as key)

```py
graph = defaultdict(list)
for u, v in edges:
    heapq.heappush(graph[u], [scores[v], v])
    if len(graph[u]) > 3:
        heapq.heappop(graph[u])
    heapq.heappush(graph[v], [scores[u], u])
    if len(graph[v]) > 3:
        heapq.heappop(graph[v])
```

then we just iterate all possible combination:
```py
res = -1
for u, v in edges:
    score = scores[u] + scores[v]
    for scoreA, a in graph[u]:
        if a == u or a == v: continue
        for scoreB, b in graph[v]:
            if b == a or b == u or b == v: continue
            res = max(res, score+scoreA+scoreB)
return res
```