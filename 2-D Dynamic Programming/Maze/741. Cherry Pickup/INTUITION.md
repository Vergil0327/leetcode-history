# Intuition

如果是一條路徑從左上到右下的話，dp會是:

dp[i][j]: the maximum number of cherries we can pick up at (i, j)

狀態轉移則為:
`dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j] if grid[i][j] != -1`

因此，這題最重要的突破口是如果是左上到右下再從右下到左上的話，我們其實可以想成有兩題路徑從左上到右下，然後用四個狀態來記錄當前最大值
並且這兩條路徑在走的時候，步數必須是一樣的

dp[i][j][x][y]: the maximum number of cherries we can pick up when we at (i, j) and (x, y)

那麼狀態轉移就是四層循環
```py
for i in range(1, n+1):
    for j in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                # dp state transfer ...
```
但由於（i, j)跟(x, y)都是一步一步走的，所以他們的步數必須是相等的
因此 `y = i + j - x if y in bounds`
所以其實我們可以省下一個維度:
`dp[i][j][x]: the maximum number of cherries we can pick up when we at (i, j) and (x, y) where y = i+j-x`

那因為每一格dp都依賴於左側跟上方的dp，所以我們可以改成**1-indexed**會比較方便

由於要取最大值，所以初始值設為`-inf`
同時如果最後答案為`-inf`，那就代表我們無法從左上順利走到右下

```py
dp = [[[-inf] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        for x in range(1, n+1):
            y = i+j-x
            if y < 0 or y > n: continue
            # dp state transfer ...
```

那麼狀態轉移就跟一條路徑走迷宮一樣
(i, j) 就看 (i-1, j) 跟 (i, j-1)
(x, y) 就看 (x-1, y) 跟 (x, y-1)
然後如果(i, j) == (x, y), 那麼cherry就只能採收一次
所以狀態轉移就為:
```py
# 1-indexed
dp[i][j][x] = max(dp[i][j][x], dp[i-1][j][x-1])
dp[i][j][x] = max(dp[i][j][x], dp[i][j-1][x-1])
dp[i][j][x] = max(dp[i][j][x], dp[i][j-1][x])
dp[i][j][x] = max(dp[i][j][x], dp[i-1][j][x])
if (i, j) != (x, y):
    dp[i][j][x] += grid[i-1][j-1] + grid[x-1][y-1]
else:
    dp[i][j][x] += grid[i-1][j-1]
```

那麼最終答案就是看我們走到(n, n) (1-indexed)的最大cherries: `dp[n][n][n] if dp[n][n][n] != -inf else 0`

最後再注意一下起點
在左上角起點的時候 (i = j = x = y = 1) -> **1-indexed**
我們得單獨處理一下
不然如果他的狀態都來自於`-inf`的話，最後得到的也會是`-inf`, 所以:
```py
dp[i][j][x] = grid[i-1][j-1] # 1-indexed
```

# Complexity

- time complexity
$$O(n^3)$$

- space complexity
$$O(n^3)$$