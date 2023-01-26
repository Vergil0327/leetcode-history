# Intuition

**definition**
dp[i][j]: the number of different arrays consist of numbers from 1 to i such that there are exactly j inverse pairs.

ex. [X X X X X] + O -> i 個組合和 j 個 inversed pairs, 額外加個數 `Ｏ`

[[O X X X X X]] -> O跟i-1個X都形成j個inversed pairs, dp[i][j] += dp[i-1][j-(i-1)]
[X [O X X X X]] -> O跟i-2個X都形成j個inversed pairs, dp[i][j] += dp[i-1][j-(i-2)]
[X X [O X X X]] -> ....
[X X X [O X X]] -> 貢獻2個inversed pair, dp[i][j] += dp[i-1][j-2]
[X X X X [O X]] -> 貢獻1個inversed pair, dp[i][j] += dp[i-1][j-1]
[X X X X X [O]] -> 貢獻0個inversed pair, dp[i][j] += dp[i-1][j-0]

**state transfer**
dp[i][j] = dp[i-1][j-m] where m = 0, 1, 2, 3, ..., i-1

```py
MOD = int(1e9+7)
for i in range(1, n+1):
    for j in range(1, k+1):
        for m in range(0, (j, i-1)+1):
            dp[i][j] += dp[i-1][j-m]
            dp[i][j] %= MOD
return dp[n][k]
```

**base case**
0個inversed pair -> 只可能有一種情形，那就是由小到大排列

```py
for i in range(1, n+1):
    dp[i][0] = 1
```

# Complexity

- time complexity
$$O(n^3)$$

- space complexity

$$O(n^2)$$

# Optimized

dp[i][j] = dp[i-1][j-m] where m = 0, 1, 2, 3, ..., i-1
dp[i][j-1] = dp[i-1][(j-1)-m] where m = 0, 1, 2, 3, ..., i-1
兩式相減得到: `dp[i][j] - dp[i][j-1] = dp[i-1][j-0] - dp[i-1][j-i]`
因此: `dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]`

reduce time complexity to $O(N^2)$