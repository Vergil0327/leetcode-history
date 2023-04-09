# Intuition

這題一開始的想法就是用topological sort

我們可以一個一個node來看來處理
如果最後processed_nodes不等於總數的話，那代表有cycle產生

同時在一開始建立adjacency node的時候
如果指向自己的話那代表有self-cycle, 可直接返回`-1`
```py
for u, v in edges:
    if u == v: return -1 # got self-cycle
```

再來就是我們把每一個可能的topological order都記錄下來
我們用一個dp[node][color]來紀錄

dp[node][color]: the maximum number of nodes until `node` when current color is `color`

對於當前這個node來說，他肯定是接在前一個node的同顏色上
所以:
```py
dp[next_node][color] = max(dp[next_node][color], dp[curr_node][color]+1)
res = max(res, dp[next_node][color])
```

另外我們在更新的同時也能順便更新一下全局`res`

這邊要注意的是，我們是放在內循環內更新`res`：
```py
for nei, color_nei in graph[node]:
    # 更新DP
```

所以在一開始找indegree = 0時也要更新
不然我們會沒進到循環而沒處理到edge case:
ex. edges = [], colors = "a"

```py
for node, deg in enumerate(indeg): # node, color
    if deg == 0:
        queue.append([node, colors[node]])
        dp[node][colors[node]] = 1
        res = 1
```

再來就是最重要的的地方

一開始我是這樣更新DP的, 這次是有誤的:

```py
dp = [defaultdict(int) for _ in range(n)]

for nei, color_nei in graph[node]:
    dp[nei][color] = max(dp[nei][color], dp[node][color] + 1)
```

但這樣我們會遺失掉這輪沒更新的所有顏色的dp值
所以我們在需要把沒更新到的顏色也都複製過去

因為根據定義，dp[node][color]是指直到node為止為color顏色的最大數目, 所以他至少會是前一輪的數量

如果用3個維度表示的話, dp應該是dp[i][node][color], 其中i代表每一輪的dp, 因此:
`dp[i] = dp[i-1]`

所以dp更新應該是:
```py
for nei, color_nei in graph[node]:
    for color in "abcdefghijklmnopqrstuvwxyz":
        dp[nei][color] = max(dp[nei][color], dp[node][color] + (1 if color == color_nei else 0))
```

