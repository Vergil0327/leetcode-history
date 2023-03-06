# Intuition

首先想到的是，如果是一般情況要求最大max sum of subarray
可以很快想到 `dp[i] = max(dp[i-1]+arr[i], arr[i])`

所以我們可以以此為基礎，挑一個數來平方

我們可以這麼定義兩種狀態的subarray

```
dp[i][0]: the maximum sum without square considering arr[:i]
dp[i][1]: the maximum sum with square operation to arr[i] considering arr[:i]
```

那麼狀態轉移的話:
dp[i][0]就是一般情況: `dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])`
dp[i][1]則可以分成三種情況:
    1. 將當前arr[i]平方，那我們跟一般情形一樣兩種情形取最大
        -  是`max(dp[i-1][0]+arr[i]**2, arr[i]**2)`
        -  看連續subarray跟自身平方哪個大
    2. 不將當前的arr[i]平方，那就是`max(dp[i-1][1] + arr[i], arr[i])`
    3. 由於arr[i]**2 >= arr[i] 所以省略掉arr[i]項

最終狀態轉移就是:

```
dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
dp[i][1] = max(dp[i-1][0] + arr[i]**2, arr[i]**2, dp[i-1][1] + arr[i])
```
        