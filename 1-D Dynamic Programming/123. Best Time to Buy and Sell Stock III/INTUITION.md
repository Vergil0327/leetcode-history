# 4 state transfer

## Intuition


**Definition**
since2 transactions at most, we can define 4 states: `hold1`, `sold1`, `hold2`, `sold2`

`hold1`: maximum money after buy 1st stock
`sold1`: maximum money after sold 1st stock
`hold2`: maximum money after sold 1st stack and buy 2nd stock
`sold2`: maximum monry after sold 2nd stock

k-1 day          k day
hold1     ->     hold1, -prices[k]
              keep holding or buy current stock with cost -price[k].
              since this is 1st stock, original money is 0

sold1     ->     sold1, hold1+prices[k]
              keep holding or sell stock and earn prices[k]

hold2     ->     hold2, sold1-prices[k]
              keep holding or buy current stock with cost -price[k]
              since this is 2nd stock, original money comes we have is from sold1

sold2     ->     sold2, hold2+prices[k]
              keep holding or sell stock and earn prices[k]
              and this is transfered from hold2 state

# bottom-up DP

**Definition**

dp[i][k][0]: means the maximum money without holding stock state after i-th day with k-transaction limitation
dp[i][k][1]: means the maximum money with holding stock state after i-th day with k-transaction limitation

**State transfer function**

`dp[i][k][0] = max(dp[i-1][k][0], dp[i][k][1]+prices[i])` # keep holding stock or sold stock and earn prices[i] money

`dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])` # keep skipping stock or buy current stock.

```
dp[i][k][1] = dp[i-1][k-1][0]-prices[i]

狀態 k 的定義不是「已進行的交易次數」
而是「最大交易次數的上限限制」。今天進行一次交易，且截至今天最大交易次數上限為 k，那么昨天的最大交易次數上限一定是 k - 1。
這樣k-1加上今天的交易，最大交易次數上限才會為 k
```