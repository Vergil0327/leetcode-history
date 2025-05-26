# Intuition

找出每個節點的深度: depth[node] = depth[parent] + 1
那這樣對於每個queries[i] = [ui, vi], 我們可以找出LCA(ui,vi)並計算出兩個節點的深度差距, 就能知道這之間有多少個邊可以加上weight

path = depth[v]-edges[LCA(ui, vi)] + depth[u]-edges[LCA(ui, vi)] where LCA is lowest common ancestor


我們目的是最後的path cost是奇數, 所以:

k of the d edges are assigned 1, and
d - k are assigned 2
Then total cost = 1 * k + 2 * (d - k) = 2 * d - k, and you want this to be odd.
That means 2 * d - k is odd ⇒ k is odd.
So, the answer is : Number of ways to choose an odd number of edges out of d to assign weight 1.

每個邊可以是`odd`或`even`, 總共有`2^path`種可能, 其中只有一半可能是奇數, 所以:

The number of ways to choose an odd count of 1s among path edges is `2^path // 2 = 2^(path-1)`.

也就是`pow(2, path - 1, 10**9 + 7)`

有了這思路後, 我們分別預處理`LCA`及`depth`:

```py
n = len(edges) + 1
        
lca = LCA(n+1, edges, 1)
graph = [[] for _ in range(n+1)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

depth = [0] * (n+1)
def dfs(node, prev, depth):
    for nxt in graph[node]:
        if nxt != prev:
            depth[nxt] = depth[node] + 1
            dfs(nxt, node, depth)
dfs(1, -1, depth)
```

那最終答案為:

```py
res = []
for u, v in queries:
    if u == v:
        res.append(0)
        continue
    depth_lca = depth[lca.get_lca(u, v)]
    path = depth[u]-depth_lca + depth[v]-depth_lca
    res.append(pow(2, path-1, 1000000007))
return res
```