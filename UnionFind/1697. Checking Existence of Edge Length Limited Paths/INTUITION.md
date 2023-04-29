# Intuition

一開始一直想著能不能用找出queries需要的每個點跟點之間的最短路徑
但這樣至少也會是個 O(Q*(E+V)), 肯定會超時

```py
graph = defaultdict(dict)
for u, v, dist in edgeList:
    if v not in graph[u]:
        graph[u][v] = dist
    else:
        graph[u][v] = min(graph[u][v], dist)
    if u not in graph[v]:
        graph[v][u] = dist
    else:
        graph[v][u] = min(graph[v][u], dist)

query = defaultdict(lambda: defaultdict(list))
for idx, q in enumerate(queries):
    u, v, limit = q
    query[u][v].append((limit, idx))

res = [False] * len(queries)
dist = [[inf]*n for _ in range(n)]
for u in query.keys():
    queue = deque([(u, 0)])
    while queue:
        for _ in range(len(queue)):
            node, d = queue.popleft()
            dist[u][node] = min(dist[u][node], d)
        
            for nei in graph[node].keys():
                distance = max(d, graph[node][nei])
                if distance < dist[u][nei]:
                    queue.append([nei, distance])
for u in  query.keys():
    for v in query[u].keys():
        for limit, idx in query[u][v]:
            res[idx] = dist[u][v] < limit

return res
```

這時應該回頭再仔細看一遍敘述
我們要求的是在每個limit下能不能從A抵達B點
這其實代表著:**在limit以下的邊我們都能走**

所以我們可以將queries跟edgeList都由小到大排序
這樣我們由小到大來看queries[i]的limit時, 我們能用的邊也同時逐個增加
這時我們就該想到我們可以用個Union-Find來處理這類型的問題

我們limit由小到大來看
當edgeList[i]的距離小於limit時, 我們便能把兩個點連接起來
這時我們僅需要用O(1)的時間透過Union-Find來查看, 這時query的兩個點有沒有在union-find裡
- 如果有, 代表我們能透過distance < limit的邊抵達
- 如果沒有在當前的union-find裡, 代表我們沒辦法透過distance < limit的邊抵達

這時整個解法的邏輯就相當清晰了

1. 分別對`edgeList`跟`queries`以**distance**及**limit**排序
   - 記得紀錄一下原始`queries`的index
 
    ```py
    for i, q in enumerate(queries):
        q.append(i)
    q = sorted(queries, key=lambda x:x[2])
    edgeList.sort(key=lambda x:x[2])
    ```

2. 我們由小到大來看queries[i], 把所有distance嚴格小於`queries[i].limit`的邊都加入到Union-Find裡

    ```py
    i = 0
    for u, v, limit, idx in q:
        while i < len(edgeList) and edgeList[i][2] < limit:
            a, b = edgeList[i][0], edgeList[i][1]
            union(a, b)
            i += 1
    ```

3. 查看當前兩點有沒有在union-find裡, 有的話代表在當前limit下, 我們手邊能用的edge能讓我們從u抵達v
    ```py
    res = [False] * len(queries)
    for u, v, limit, idx in q:
        # union step ...

        pu, pv = find(u), find(v)
        if pu == pv:
            res[idx] = True
    ```

# Complexity

- time complexity
$$O(ElogE)$$

- space complexity
$$O(N)$$