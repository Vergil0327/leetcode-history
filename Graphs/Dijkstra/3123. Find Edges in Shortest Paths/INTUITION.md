# Intuition

這題當下沒做出來, 事後檢討才發現是腦袋卡死
其實這題很簡單

首先這題要的就是找出所有shortest path, 然後查看edges[i]能不能組成一條shortest path

我們都知道可以用Dijkstra找出shortest path的cost是多少, 那有了這個條件後該如何找出所有shortest path?
當時想的是BFS, DFS都會超時, 但實際上我們並不需要找出所有可能的shortest path

首先我們看src->dst這條路徑, 表示成:

```
src -> X -> Y -> Z -> dst
```

假設shortest path的cost是`cst`
那麼如果X->Y能組成shortest path的話, 他的cost也必須等於`cst`, 也就是必須滿足:`cost[src][X] + X->Y + cost[Y][dst] == cst`

那有了這條件之後, 我們就能利用這條件來查看edges[i]是不是能組成合法shortest path了

我們只需要遍歷edges[i], 然後查看:

- 首先定義edges[i] = [u,v,w]
- 如果edges[i]是shortest path的一部分, 那麼他必須滿足任一條件:
   1. src -> u -> v -> dst = cost[src][u] + w + cost[v][dst] == cst
   2. src -> v -> u -> dst = cost[src][v] + w + cost[u][dst] == cst
   3. shortest path可能是從`src -> u -> v -> dst`, 也可能是`src -> v -> u -> dst`

那麼我們僅需要預處理cost[src][node], cost[node][dst]即可, 而這正好就是dijkstra會求得的

```py
def dijkstra(src, dst):
    cost = [inf]*n
    cost[src] = 0
    
    pq = [(0,src)]
    seen = set()
    while pq:
        wei, node = heapq.heappop(pq)
        if node in seen: continue
        seen.add(node)
        cost[node] = wei

        for nxt in graph[node]:
            if wei+graph[node][nxt] < cost[nxt]:
                heapq.heappush(pq, [wei+graph[node][nxt], nxt])
    return cost

costFromSrc = dijkstra(0, n-1)
costFromDst = dijkstra(n-1, 0)
```

求出來後我們遍歷edges[i]查看能不能組成shortest path即可:
- isShortedpath = costFromSrc[u] + w + costFromDst[v] == minCost or costFromSrc[v] + w + costFromDst[u] == minCost

- edge case: src 跟 dst 沒有相互連接 => `minCost == inf`


time: O(ElogV + edges.length)