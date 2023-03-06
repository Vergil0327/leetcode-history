# Intuition

這題目的是要找一個有min distance的path，根據editDistance的定義可得知，我們要找的path長度必須等於targetPath

首先先不管路徑，如果要求minDistance的話，那就是個明顯的DP問題，我們根據題意可以這樣定義


dp[i][target]: the minimum distance to reach `target` city at `i` position

那麼狀態轉移很明顯為：
`dp[i][target] = dp[i-1][city] + (1 if target != targetPath[i] else 0) where city can reach target`
其中city 可以從adjacency list得知

所以整個框架為:
遍歷m個位置，然後遍歷n個city進行dp[i][target]的狀態轉移

city為與`target`相鄰的所有城市

**base case**
由於起點可以是任意位置，而且沒有dp[0-1]，所以我們單獨處理

```py
graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
m = len(targetPath)
dp = [[float('inf')]*n for _ in range(m)]
for i in range(n):
    dp[0][i] = 1 if names[i] != targetPath[0] else 0

for i in range(1, m):
    for target in range(n):
        for city in graph[target]:
            dp[i][target] = min(dp[i][target], dp[i-1][city] + (1 if names[target] != targetPath[i] else 0))
```

但由於題目要求的是符合min distance的任意path，所以我們再另外利用`prev[i][target] = city`紀錄我們走的路徑

```py
for i in range(1, m):
    for target in range(n):
        for city in graph[target]:
            dist = dp[i-1][city] + (1 if names[target] != targetPath[i] else 0)
            if dist < dp[i][target]:
                dp[i][target] = dist
                prev[i][target] = city
```

這樣我們最後再從最終解反推回來即可

最後一個位置是確定的，那就是 `min(dp[m-1])`
```py
dist = float('inf')
city = -1
for i in range(n):
    if dp[m-1][i] < dist:
        dist = dp[m-1][i]
        city = i
```

然後再利用prev的資訊一路逆著走回來，最後在把整個路徑反過來即為答案