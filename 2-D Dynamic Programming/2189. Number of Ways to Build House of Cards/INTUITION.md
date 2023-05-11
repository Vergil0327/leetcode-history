# Intuition

```
/\

 __
/\/\

 ____
/\/\/\

每一層: 2 +3 +3 +3 +3

 /\
 __
/\/\

往上疊: (2+3+3...) + (2+3+3...)
```

以單層來看, 單層用的牌數為: 2 + 3*(k-1)

如果我們全部用來搭建單層, `代表 2+3*(k-1) == n`時才有1個方法解

再來我們試著這樣設計dp:
`dp[i][j]: the number of distinct card-house we can build for i levels of card-house by using j cards totally`

然後我們著眼於第`i`層:
- 如果我們不搭建第`i`層, 那就看`dp[i-1][j]`
- 如果我們選擇搭建第`i`層, 那就看剩下沒用的牌來組成前面`i-1`層的合法方法數有多少, `dp[i][j] = dp[i-1][j - current used cards] = dp[i-1][j - 2+3*(i-1)]`
  - 構建第一層需要 2+3*(i-1) where i = 1
  - 構建第二層需要 2+3*(i-1) where i = 2

那麼狀態轉移為:

dp[i][j] = dp[i-1][j] + dp[i-1][j - 2+3*(i-1)] where i starts from 1 to `i//2` and `0 <= j <= n`

ex. 7張卡能組兩層, 大略計算一下`i`張卡不超過`i//2`層
