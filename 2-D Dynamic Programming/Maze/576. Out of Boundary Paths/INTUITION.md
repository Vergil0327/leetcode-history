# Intuition

## topdown
DFS based on constraints

we can start DFS from (`startRow`, `startColumn`) and only can take `maxMoves` step.
whenever we reach `r < 0` or `r == m` or `c < 0` or `c == n` within `maxMoves` steps, it means we found 1 way to out-of-bounds.


## bottom-up

首先一個很自然的想法是，如果我們從(startRow, startColumn)出發
我們要bottom-up的話我們要由中心往外擴散，先知道走1步直到maxMove步後，這期間抵達邊界的次數
並不好解

但如果有想到DFS solution, 或是反向思考一下的話
其實我們可以改從邊界出發，然後看走到(startRow, startColumn)時有幾種走法

由於我們總共可以走`maxMove`步
我們可以這樣定義dp[r][c][k]: the number of ways to reach (r, c) within `k` steps

那對於(r, c)來說，他可以從四個方向抵達，所以是加上那四個方向的方法數

```py
dirs = [[-1,0], [1,0], [0, 1], [0, -1]]
for dr, dc in dirs:
    row, col = r+dr, c+dc
    dp[r][c][move] += dp[row][col][move-1]
    dp[r][c][move] %= MOD
```

最終答案就是看我們花maxMove步有多少種方法抵達(startRow, startColumn): `dp[startRow+1][startColumn+1][maxMove]`
startRow+1, startColumn+1 是因為我們dp有多橫移一格給邊界

**base case**

由於我們要從邊界出發，所以我們四個方向都多一格
遍歷範圍變成[1, m+1]跟[1, n+1]
`dp = [[[0]*(maxMove+1) for _ in range(n+2)] for _ in range(m+2)]`

四個邊界，不管我們當下是走第幾步，方法數都是1

```py
for r in range(m+2):
    for move in range(maxMove+1):
        dp[r][0][move] = 1
        dp[r][n+1][move] = 1

for c in range(n+1):
    for move in range(maxMove+1):
        dp[0][c][move] = 1
        dp[m+1][c][move] = 1
```