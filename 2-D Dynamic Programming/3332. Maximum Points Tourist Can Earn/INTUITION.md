# Intuition

每個城市可以自由前往其他城市, 代表整個graph是全連結的
一開始想說把所有可能用max heap裝進去, 但發現這樣space會展開太大

所以後來想到我們可以用個dp紀錄每天每個節點的最高分

dp[i][j]: the maximum score for node `j` at i-th day

那再來就遍歷所有可能更新dp[i][j]即可, 狀態轉移也很直覺

首先兩層循環遍歷`i`, `cur`, 然後再遍歷下個可能的去處`nxt`:

- 如果`cur == nxt`, 代表我們選擇stayScore[i][cur]
  - dp[i+1][cur] = dp[i][cur] + stayScore[i][cur]
- 如果`cur != nxt`, 代表我們選擇travelScore[cur][nxt]
  - dp[i+1][nxt] = dp[i][cur] + travelScore[cur][nxt]

```py
for i in range(k):
    for cur in range(n):
        for nxt in range(n):
            if nxt == cur:
                dp[i+1][cur] = max(dp[i+1][cur], dp[i][cur] + stayScore[i][cur])
            else:
                dp[i+1][nxt] = max(dp[i+1][nxt], dp[i][cur] + travelScore[cur][nxt])
```

那這樣最終答案就是在k-th day從每個節點找最高分: `max(dp[k])`

# Complexity

time: O(k * n * n)

space: O(k * n)