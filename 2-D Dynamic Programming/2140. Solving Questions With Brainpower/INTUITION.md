# Intuition

first thought, house robber with k neighbor constraints ?

如果說, 我們定義:
- dp[i]: the maximum points considering questions[i:] problems

```
X X X X X X {X X X X X X X} X
          i i+1         i+k j
        solve    skip     solve
```

那狀態轉移應該就是當下solve與否:
- 如果我們解決questions[i], 那麼question[i+1]到question[i+k]都不能解. `dp[i] = dp[j]+score`
- 如果我們選擇不解決question[i], 那麼就是dp[i+1]

這樣看起來dp[i]會依賴於後面的dp值, 所以我們可能得從後面往前面遍歷
小心越界問題, dp[n-1]先提早處理

```
dp[n-1] = questions[n-1][0]
for i in range(n-2, -1, -1):
    score, k = questions[i]
    dp[i] = max(dp[i+1], (dp[i+k+1] if i+k+1 < n else 0)+score)

return dp[0]
```

那最終答案應為`dp[0]`