# Intuition

1 <= n <= 10 => 數據極小, 可以用bitmask進行狀態壓縮來代表我們所選擇的closed set
ex. 100010 => 1代表示closed的

再來我們就能遍歷所有可能的closed set, O(2^n) = 1024

然後我們在檢查那些non-closed node能不能在maxDistance內抵達所有其他節點即可 => 對每個節點進行BFS+pq (Dijkstra)?

觀察一下時間複雜度會發現 n <= 10, 所以我們可以用O(n^3)的floyd algorithm來建構任意兩點的最短路徑

```py
for start in range(n):
    for end in range(n):
        for mid in range(n):
            dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid][end])
```

# Complexity

那這樣總時間複雜度約為O(2^n * (n^3 + roads.length)) ~ $10^6$