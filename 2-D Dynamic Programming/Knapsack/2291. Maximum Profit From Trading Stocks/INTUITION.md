# Intuition

經典背包問題，我們有這麼多的容量 `budget`, 然候我們可以選擇這些物品 `present[i]`
選擇第i項物品所能獲得的量為 `future[i]-present[i]`

所以我們可以這麼定義dp:

dp[i][j]: the maximum amount of profit for i-th selection with j budget

那狀態轉移則為:
- 不選擇第i項物品: dp[i][j] = dp[i-1][j]
- 選擇第i項物品: dp[i][j] = dp[i-1][j-present[i]] + (future[i] - present[i])
  - 那麼前一個狀態則為 `j-present[i]`, 加上這第i項後budget=j

那最終答案就是dp[n][budget] (1-indexed) -> 背後意義是考慮n項物品及budget

由於dp[i-1]在i=0時會越界，所以我們用1-indexed, 遍歷範圍改為[1:n]
```py
n = len(present)
present = [0] + present
future = [0] + future
profit = [future[i]-present[i] for i in range(n+1)]

dp = [[-float("inf")] * (budget+1) for _ in range(n+1)]
```

**base case**

0項物品，不管多少budget, 最高profit都是0

```py
for j in range(budget+1):
    dp[0][j] = 0
```