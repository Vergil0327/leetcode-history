# Intuition

這題比較tricky的地方是，數值有正有負
最小的negative value再乘上一個負數後有可能會變成最大的正數
因此最小的數跟最大的數我們都必須記錄下來

因此我們可以定義dp為一個size=2的array:

dp[i][j][0]: the maximum product path at (i, j)
dp[i][j][1]: the minimum product path at (i, j)

因此對dp[i][j]來說他可以從dp[i-1][j]跟dp[i][j-1]轉移過來
並且dp[i-1][j]跟dp[i][j-1]都各自有兩個狀態

所以就是從四個狀態中轉移過來，四個中取最小作為dp[i][j][0], 最大作為dp[i][j][1]

```py
for i in range(m):
    for j in range(n):
        dp[i][j][0] = min(dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j], dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j])
        dp[i][j][1] = max(dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j], dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j])
```

最終答案就是the maximum product path: `dp[m-1][n-1][1]%int(1e9+7) if dp[m-1][n-1][1] > 0 else -1`

再來我們注意下標
由於i=0或j=0時dp有可能越界, 所以i=0跟j=0這兩種情況我們單獨處理

**base case**
`dp[0][0] = [grid[0][0], grid[0][0]]`

由於i=0跟j=0時都只能從一個方向轉移過來
所以最小值跟最大值都會是前一個狀態乘上當前的grid[i][j]
```py
# j=0
for i in range(1, m):
    v = dp[i-1][0][0] * grid[i][0]
    dp[i][0] = [v, v]
# i=0
for j in range(1, n):
    v = dp[0][j-1][0] * grid[0][j]
    dp[0][j] = [v, v]
```