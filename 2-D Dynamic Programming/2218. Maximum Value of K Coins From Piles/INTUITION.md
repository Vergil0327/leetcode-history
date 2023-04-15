# Intuition

dp[i][j]: the maximum total value considering first i piles and choosing j coins

[X X X] X X X X X X
[X X X X X X] X X X
[X X X X] X X X X X  -> i-th pile

這題很明顯能看出是個DP題
可以先試著定義dp為:
`dp[i][j]: the maximum total value considering first i piles and choosing j coins`

那這樣的話我們關注piles[i]
如果我們對當前的piles[i]取`k`個, 那麼在前i-1個piles裡我們應該已經取了dp[i-1][j-k]個, 然後總共取j個
然後從上面示意圖可知, 我們還會需要個prefix sum來幫助我們查找前`k`個的總和為多少

所以狀態轉移可以很快地寫出:
```py
dp = [[-inf] * (K+1) for _ in range(n)]
for i in range(n):
    m = len(piles[i])
    for j in range(K+1):
        for k in range(min(j, m)+1):
            dp[i][j] = max(dp[i][j], (dp[i-1][j-k] if i-1>=0 else 0) + presum[i][k])
```

那麼最終答案就是dp[n-1][K]

# Complexity

- time complexity

我們會發現有三層循環: O(n * K * ?)
但實際上這三層循環的最外兩層也能調換下順序, 並不影響dp狀態的更新

```py
dp = [[-inf] * (K+1) for _ in range(n)]
for j in range(K+1):
    for i in range(n):
        m = len(piles[i])
        for k in range(min(j, m)+1):
            dp[i][j] = max(dp[i][j], (dp[i-1][j-k] if i-1>=0 else 0) + presum[i][k])
```

這樣一看會發現裡面的兩層循環, 其實就是遍歷所有piles[i][j]

```py
for i in range(n):
    for k in range(min(j, m)+1):
        # update dp[i][j]
```

那根據constraints: `sum(piles[i].length) <= 2000`
所以時間複雜度為:

$O(n * K * ?)$ = $O(K * (n*?))$ = $O(K * 2000)$