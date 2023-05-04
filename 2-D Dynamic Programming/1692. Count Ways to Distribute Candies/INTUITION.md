# Intuition

k bags = K K K K K K K K

candies = X X X X X X X X X X X X X X
                                  i

for candies[i]:
1. 放在新的袋子, 不管是哪個都一樣, 方法數 += 1
2. 放在已經有糖果的袋子, 每個組合方法都不一樣, 方法數 += 所有組合方法

所以定義dp[i][j]: the number of different ways to distribute first i candies to first j bags

1. dp[i][j] += dp[i-1][j-1]
   - 前面`i-1`個糖果僅用前面`j-1`個袋子
2. dp[i][j] += dp[i-1][j] * j
   - 前面`i-1`個糖果用`j`個袋子, `j`個選擇都不同

所以狀態轉移則為
```py
for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] += dp[i-1][j-1] + dp[i-1][j] * j
        dp[i][j] %= 1_000_000_007
return dp[n][k]
```

再來由於我們`i`, `j`範圍個別是從`[1:n]`跟`[1:k]`
會用到dp[0][0]跟dp[0][1], 這些都沒有賦值

接下來考慮`dp[0][j]`跟`dp[i][0]`
當`i=1`時, 會有1個糖果分給0個袋子這種情況
當`k=1`時, 0個糖果分給1個袋子, 也是0
這樣全部都是0, dp狀態不會更新

由於我們每個袋子都必須分到糖果, 所以從1個糖果開始必須至少要有1個袋子
這樣dp值才有辦法繼續更新下去

所以j=1我們單獨處理, j從[2:k]開始更新

前i個糖果放到1個袋子, 那就只有1個方法
```py
for i in range(1, n+1):
    dp[i][1] = 1
```
