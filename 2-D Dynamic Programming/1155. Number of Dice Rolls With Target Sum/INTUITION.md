# Intuition

一開始直接想到的是我們可以這麼定義:

**dp[i][j][k]: the number of ways to make sum be `j` and the die ended at `k` at `i-th` rolls**

那這樣狀態轉移也很理所當然, 對於當前dp[i][j][k]來說, 他的前驅狀態可以是骰子的任意一個面, 所以遍歷[1, k]全加總起來

```py
for m in range(1, k+1):
    dp[i][j][k] += dp[i-1][j-k][m]
```

但仔細觀察可發現, 其實我們並不需要紀錄`k`, `m`這些資訊
所以我們可以改成這麼定義:

**dp[i][j]: the number of ways to make sum be `j` at `i-th` roll**

那這樣我們的狀態更新外圈就是[1,n], 內圈就遍歷所有可能target[1, target]
那由於前驅狀態有k種可能, 把停在`k`面骰子的可能性全部加總起來
```py
for i in range(1, n+1):
    for t in range(1, target+1):
        for j in range(1, k+1):
            if t-j >= 0:
                dp[i][t] += dp[i-1][t-j]
```

那最終答案就是`dp[n][target]`

# Optimization

由於dp[i][t]只依賴於前一個狀態dp[i-1][t-j]
所以我們可以用兩個dp[target] array來儲存資訊即可

```py
dp1 = [0 for _ in range(target+1)]
dp2 = [0 for _ in range(target+1)]
dp1[0] = 1
for i in range(1, n+1):
    for t in range(1, target+1):
        for j in range(1, k+1):
            if t-j >= 0:
                dp2[t] += dp1[t-j]
                dp2[t] %= 1000000007
    dp1, dp2 = dp2, [0 for _ in range(target+1)]
return dp1[target]
```

# Complexity

- time complexity
  $$O(n * target * k)$$

- space complexity
    $$O(2 * target)$$