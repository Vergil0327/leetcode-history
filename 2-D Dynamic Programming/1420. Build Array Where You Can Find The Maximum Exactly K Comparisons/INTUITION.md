# Intuition

一開始的想法是:
因為我們在意的是當下的arr[i]跟到目前為止的maximum_value `mx`, 所以試著這樣定義dp
dp[i][mx][k]: the number of way at i-th rounds with current maximum value is mx (= max(arr[1:i-1])) and search_cost is k
```py
dp = [[[0]*(K+1) for _ in range(m+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(1, n+1):
    for mx in range(m+1):
        for k in range(1, K+1):
            for curr in range(1, m+1):
                dp[i][curr][k]
                if curr > mx:
                    dp[i][curr][k] += dp[i-1][mx][k-1]
                    dp[i][curr][k] %= mod
                else:
                    dp[i][mx][k] += dp[i-1][curr][k]
                    dp[i][mx][k] %= mod
            
res = 0
for mx in range(m+1):
    res += dp[n][mx][K]
return res % mod
```

但這樣發現有個問題, `Input: n = 50, m = 100, k = 25` testcase 過不了
仔細一看發現這個表達式`dp[i][curr][k] += dp[i-1][mx][k-1]`有問題
如果當前mx為current, 那他的前一個狀態應該不只是mx, 而是所有小於`mx`的dp值

所以我們應該要更改一下dp定義為:
當前的maximum_value為`mx`, 所以試著這樣定義dp
dp[i][mx][k]: the number of way at i-th rounds with current maximum value is mx (= max(arr[1:i])) and search_cost is k

那這樣的話狀態轉移則為

```
if arr[i] = mx:
    dp[i][mx][k] += dp[i-1][j][k-1] where 1 <= j < mx

if arr[i] != mx:
    dp[i][mx][k] += dp[i-1][mx][k] for every arr[i] <= mx where 1 <= mx <= m
                 += dp[i-1][mx][k] * mx
```

並且後來發現1-indexed並沒有比較好做, dp[0][mx][k]的初始值並不好設
不如把edge case i = 0時拿出來單獨賦值
所以依舊用0-indexed

```py
dp = [[[0]*(K+1) for _ in range(m+1)] for _ in range(n)]

for i in range(n):
    for mx in range(1, m+1):
        for k in range(1, K+1):
            for curr in range(1, mx):
                dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][curr][k-1])%mod
            dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][mx][k] * mx)%mod
```

那最終答案可能落在任何一個mx, 所以全部加總即為答案
```py
res = 0
for mx in range(1, m+1):
    res = (res + dp[n-1][mx][K])%mod
return res
```

同時`for k in range(1, K+1):`也能優化一下
當index為`i`時, 最多只會有`i+1`次cost (0-indexed), 所以可以更改為
```py
for i in range(n):
    for mx in range(1, m+1):
        for k in range(1, min(i+1, K)+1):
            # update dp
```

當dp框架搭好之後，再來就是看edge case
我們發現i=0時, 會出現dp[-1]
所以單獨把`i=0`拿出來更新dp

當i=0時, 不管mx為多少, cost只會是1 (i.e. k=1)
並且arr[i]肯定是mx, 只會有這一種可能, 所以:
> p.s. 根據定義, maximum_value 一開始為`-1`

```py
# i=0
for mx in range(1, m+1):
    # for k in range(1, min(1, K)+1):
    #     dp[0][mx][k] = 1
    dp[0][mx][1] = 1

for i in range(1, n):
    for mx in range(1, m+1):
        for k in range(1, min(i+1, K)+1):
            for curr in range(1, mx):
                dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][curr][k-1])%mod
            dp[i][mx][k] = (dp[i][mx][k] + dp[i-1][mx][k] * mx)%mod
```