# Intuition

先手取走之後得到的分數會再變回一個石頭放回去
所以石頭總數其實不會變, 只是分數合併在一塊

從剩一個石頭開始推導, 可推出關係式如下

```
dp[i]: the maximum difference for i remaining stones

[X X X X X X X X O]  -> dp[i] = dp[1] = alice - bob = 0 - 0 = 0

[X X X X X X X O] O  -> dp[i] = dp[2] = alice - bob = presum[n] - dp[1]
                 
[X X X X X X O] O O  -> dp[i] = dp[3]
                              =? presum[n] - dp[1]
                              =? presum[n-1] - dp[2]
                              = max(presum[n] - dp[1], presum[n-1] - dp[2])
                              = max(dp[2], presum[n-1]-dp[2])

i = 2 -> n
i = 3 -> n-1
i = 4 -> n-2
presum[n-i+2]
```