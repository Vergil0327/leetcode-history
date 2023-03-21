# Intuition

求最大路徑和是很明顯的dynamic programming問題
我們可以定義 `dp[i][j]: the maximum sum of numeric characters we can collect when reached (i, j)`

由於從右下走到左上跟左上走到右下是一樣的, 只是遍歷的方向相反
所以我們從左上走到右下, 對於dp[i][j]來說，他可以從三個狀態轉移過來:
- dp[i-1][j]
- dp[i][j-1]
- dp[i-1][j-1]
所以我們就三者取**max**再加上 `board[i][j] if board[i][j].isdigit() else 0` 即可

```py
dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
score = int(board[i-1][j-1]) if board[i-1][j-1].isdigit() else 0
dp[i][j] += score
```

比較要注意的是路徑的求法
很明顯也是DP問題，我們可以用另一個array來求
定義 path[i][j]: the number of paths to maximum path sum we can get to reach (i, j)

同樣對於path[i][j]來說, 一樣可以從三個方向轉移過來:
- path[i-1][j]
- path[i][j-1]
- path[i-1][j-1]

但要注意的是，這三個方向是獨立的
如果三個方向抵達(i, j)後，path sum都為我們前面計算出的maximum path sum, 那這三個方向的路徑都是解
所以是三個獨立的加法

因此我們要做的是:
1. 判斷當前的最大path sum是從哪個方向轉移過來, 三個獨立的if判斷
2. 把這些方向的path數都相加起來
3. 記得對1e9+7取餘數

```py
dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
if dp[i-1][j] == dp[i][j]:
    path[i][j] += path[i-1][j]
    path[i][j] %= MOD
if dp[i][j-1] == dp[i][j]:
    path[i][j] += path[i][j-1]
    path[i][j] %= MOD
if dp[i-1][j-1] == dp[i][j]:
    path[i][j] += path[i-1][j-1]
    path[i][j] %= MOD
```
