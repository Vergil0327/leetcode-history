# Intuition

一開始想到brute force為:

我們定義dp[i][x][y][z]: 考慮前i位, 至少包含`x`個**l**, `y`個**e**, 跟`z`個**t**的string的組合方法數有多少

那麼最終答案就是dp[n][1][2][1], n位數裡有至少1個`l`, 2個`e`, 1個`t`
並且我們都加個cap, 加個上限, 因為超過1個的`l`跟超過2個的`e`以及超過`1`個的`t`的狀況也都是合法的

我們狀態轉移就如下
```py
for ch in range(26):
    if ch == L:
        dp[i+1][min(1, x+1)][y][z] += dp[i][x][y][z]
        dp[i+1][min(1, x+1)][y][z] %= mod
    elif ch == E:
        dp[i+1][x][min(2, y+1)][z] += dp[i][x][y][z]
        dp[i+1][x][min(2, y+1)][z] %= mod
    elif ch == T:
        dp[i+1][x][y][min(1, z+1)] += dp[i][x][y][z]
        dp[i+1][x][y][min(1, z+1)] %= mod
    else:
        dp[i+1][x][y][z] += dp[i][x][y][z]
        dp[i+1][x][y][z] %= mod
```

所以整體框架為:
```py
class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10**9 + 7
        if n < 4: return 0
        if n == 4: return 12
        
        L, E, T = ord("l")-ord("a"), ord("e")-ord("a"), ord("t")-ord("a")
        dp = [[[[0]*2 for _ in range(3)]for _ in range(2)] for _ in range (n+1)]
        dp[0][0][0][0] = 1
        for i in range(n):
            for l in range(2):
                for e in range(3):
                    for t in range(2):
                        for ch in range(26):
                            if ch == L:
                                dp[i+1][min(1, l+1)][e][t] += dp[i][l][e][t]
                                dp[i+1][min(1, l+1)][e][t] %= mod
                            elif ch == E:
                                dp[i+1][l][min(2, e+1)][t] += dp[i][l][e][t]
                                dp[i+1][l][min(2, e+1)][t] %= mod
                            elif ch == T:
                                dp[i+1][l][e][min(1, t+1)] += dp[i][l][e][t]
                                dp[i+1][l][e][min(1, t+1)] %= mod
                            else:
                                dp[i+1][l][e][t] += dp[i][l][e][t]
                                dp[i+1][l][e][t] %= mod
        return dp[n][1][2][1]%mod
```

但這樣會TLE

實際上除了L, E, T外, 其他字母是什麼我們並不關心
所以我們可以簡化成:

第i個字母選擇:
1. `i`
2. `e`
3. `t`
4. `其他`, 剩下有23種字母可選, 所以第`i-1`位方法數 * 23就是第`i`位方法數

```py
dp[i+1][min(1, l+1)][e][t] += dp[i][l][e][t]
dp[i+1][min(1, l+1)][e][t] %= mod

dp[i+1][l][min(2, e+1)][t] += dp[i][l][e][t]
dp[i+1][l][min(2, e+1)][t] %= mod

dp[i+1][l][e][min(1, t+1)] += dp[i][l][e][t]
dp[i+1][l][e][min(1, t+1)] %= mod

dp[i+1][l][e][t] += dp[i][l][e][t] * 23
dp[i+1][l][e][t] %= mod
```