# Bottom-Up DP

## Intuition

這題的profit加總可以很大，100 crimes * 100 members *  (100 * 100) Profit
如果我們用三層循環來求 `dp[i][members][profit] = dp[i-1][members][profit]+dp[i-1][members-group[i]][profit-profit[i]]`的話，不僅遍歷很花時間，記憶體需求也很大

但由於我們只需要知道大於`minProfit`的計畫個數即可，因此profixt其實是有個upperbound存在的

因此我們可以將DP定義改成:
- 當profit < minProfit時, `dp[i][members][proft]: from first i crimes, how many of schemes s.t. we just use members and earn profits`
- 但當profit >= minProfit時，此時的dp等於`dp[i][members][minProfit] + dp[i][members][minProfit+1] + dp[i][members][minProfit+2] + ...`，也就是所有profit>=minProfit的加總

此時 dp的狀態轉移也必須變換方向，必須改成類似Top-Down DP 的形式:
`從已知的dp[i][member][profit]狀態來更新下個未知的dp[i+1][member'][profit']狀態`

此時的狀態轉移方程為:
```
dp[i+1][p][g] += dp[i][p][g]
dp[i+1][min(p+profit[i], minProfit)][g+group[i]] += dp[i][p][g]
```
其中可以看到，我們透過`min(p+profit[i], minProfit)`來將profit>=minProfit的所有個數加總起來到`dp[i][minProfit]`上

- time complexity

$$O(N*MinProfit*M)$$

- space complexity

$$O(N*MinProfit*M)$$

其中M是項目個數

# Top-Down DP

## Intuition

just simulate decision tree with take-or-skip strategy

be careful of special case: `minProfit=0`. if `minProfit` equals to 0, we need to add extra scheme to answer

## Complexity

- time complexity

$$O(M*Profit*Group)$$

- space complexity

$$O(M*Profit*Group)$$

其中M是項目個數