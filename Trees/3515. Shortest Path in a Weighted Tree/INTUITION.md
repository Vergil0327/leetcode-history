# Intuition

一般來說, dijkstra框架如下:

```py
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        dp = [inf] * (n+1)
        dp[1] = 0
        pq = [1]
        while pq:
            node = heapq.heappop(pq)
            for nxt, wei in graph[node]:
                if dp[node] + wei < dp[nxt]:
                    dp[nxt] = dp[node] + wei
                    heapq.heappush(pq, nxt)
        print(dp)
        res = []
        for typ, *x in queries:
            if typ == 1:
                u, v, w = x
                # update edge (u,v) with weight w
            else:
                # compute shortest path from 1 to x
                res.append(dp[x])
        return res
```

重點在於如何在新的權重下, 高效更新`dp`

這邊會用到Euler Tour來將Tree Traversal攤平成一維array

- 標記每個節點的entry time (t_in)跟exit time (t_out)
- 標記每個節點的父節點: parent[node]
- 標記根節點到`node`節點的距離: dist[node]
- 標記每個edge的權重: weight[(min(u,v), max(u,v))] = w

```py
# euler tour
graph = [[] for _ in range(n)]
weight = {}
for u,v,w in edges:
    u -= 1
    v -= 1
    graph[u].append([v,w])
    graph[v].append([u,w])

    if v<u: u,v=v,u
    weight[u, v] = w

t_in = [0] * n
t_out = [0] * n
dist = [0] * n
parent = [0] * n
timer = 0

def dfs(u, p):
    nonlocal timer
    parent[u] = p
    timer += 1
    t_in[u] = timer

    for v, w in graph[u]:
        if v != p:
            dist[v] = dist[u] + w
            dfs(v, u)

    t_out[u] = timer
    timer += 1

dfs(0, -1)
```

那將Tree攤成一維的好處是, 我們可以用BIT (Fenwick Tree)來計算每個節點間的距離, 並提供高效range update的能力

### Range Update

假設我們現在要更新`u -> v`節點成新的權重`w'`:'
1. 首先先判斷誰是child, child才是我們的目標節點 `node`
2. 計算權重的delta = w' - weight[node]'
3. 再來透過Fenwick Tree來進行range update, 概念上會有點像是difference array
    - add delta at t_in[node] (entry time of node)
    - subtract delta at t_out[node]+1 (immediately after the exit time of node)
4. 更新weight[node] = w'

既然搞定range update, 那再來只要遍歷queries並回答即可:

> For a query [2, x], We combine the updates done on weights till now on the path from root = 1 to node x by querying the Fenwick Tree from tin[1] to tin[x] which is basically the prefix sum upto tin[x] in the FT. We combine this change (delta) with the original distance (dist[u]) to get the answer .

對於queries[j] = [2, x], 我們可以透過Fenwick Tree來得到`node-1`到`node-x`的**delta**距離 = fenwick.sum(t_in[node])
最終距離 = dist[node] + delta = dist[node] + fenwick.sum(t_in[node])

# Complexity

Time Complexity: O(logN) per update or query (due to the Fenwick Tree).
Space Complexity: O(N), for storing the Euler Tour arrays and the Fenwick Tree.