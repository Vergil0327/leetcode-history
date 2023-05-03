# Intuition

```
[X X X X X]
 i       j
 _ _ _ _ _
 _ _ _ _ *
 _ _ _ * *

 * _ _ _ _
 * * _ _ _

 * * - _ _
 * * * _ _
 * * * * _
 * * * * * 
      draw or not draw
```

一開始想法是從0為起點開始, 畫線或不畫線
但當初沒想仔細的是, 這樣其實會有問題
仔細看會發現會有重複的部分
當我們以`i`為起點開始不畫的話, 之後如果又在選擇不畫
這時會跟以`i`為起點到`i+2`間都不畫相重複, 因此我們當前的兩個狀態並不完整

```py
def numberOfSets(self, n: int, k: int) -> int:
    mod = 10**9 + 7

    @cache
    def dfs(i, k):
        if k == 0: return 1
        
        res = 0
        for j in range(i+1, n):
            res += dfs(j, k) + dfs(j, k-1)
        return res%mod

    return dfs(0, k)
```

這時要想的是, 如果要讓我們的狀態表達式能成立的話
必須在多個狀態來表示當前第`i`個點, 一定有使用或一定沒使用, 也就是:

dp[i][k][0]: the number of ways considering first i elements, and we must NOT use i-th point to draw k line segments

dp[i][k][1]: the number of ways considering first i elements, and we must use i-th point to draw k line segments


這樣的話

```
[X X X X X]
     j   i
```

1. we do not draw from j to i. the number of ways that we draw from 0 to j are valid. if we add the number of ways that we don't draw from 0 to j, ex. dp[j][k][0], it'll conflict dp[i'][k][0] where i == j
   - `dp[i][k][0] += dp[j][k][1] where 0 <= j < i`


2. we draw a line from j to i. the number of ways that we draw or not draw from 0 to j are valid
   - `dp[i][k][1] += dp[j][k-1][0] + dp[j][k-1][1] where 0 <= j < i`

那麼整體狀態轉移框架會是:
```py
class Solution_TLE:
    def numberOfSets(self, n: int, K: int) -> int:
        # dp[i][k]: considering first i points, construct k line segments

        for i in range(i):
            for k in range(min(i, K)+1):
                for j in range(i):
                    dp[i][k][0] += dp[j][k][1]
                    dp[i][k][1] += dp[j][k-1][0] + dp[j][k-1][1]
                
        return dp[n-1][K][0] + dp[n-1][K][1]
```

但這樣會是個O(N^3)的時間複雜度, 會TLE
這時比較常見的改進方式是, 仔細看內層循環, 他其實是`[0:i)`區間的dp疊加
所以我們可以用個prefix sum來儲存先前計算過的訊息

```py
for i in range(n):
    for k in range(min(i, K)+1):
        # for j in range(i):
        #     dp[i][k][0] += dp[j][k][1]
        dp[i][k][0] = presum[i-1][k][1]

        # for j in range(i):
        #     dp[i][k][1] += dp[j][k-1][0] + dp[j][k-1][1]
        dp[i][k][1] = presum[i-1][k-1][0] + presum[i-1][k-1][1]

        presum[i][k][1] = (presum[i-1][k][1] + dp[i][k][1])%mod
        presum[i][k-1][0] = (presum[i-1][k-1][0] + dp[i][k-1][0])%mod
```