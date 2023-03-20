# Topdown

## Intuition

use DFS to explore every possible solution.
since we can choose any next column if it's not adjacent with current column, we try them all.

**base case**
- if currentRow >= n, return 0
- if currentColumn out of bounds, return inf since we want to find minimum falling sum

```py
def dfs(currentRow, currentColumn):
    for nextCol in range(-1, n+1):
        if nextCol != currentColumn:
            res = min(res, dfs(r+1, nextCol))
    return res + grid[currentRow][currentColumn]
```

# Bottom-up

bottom-up也很直覺
我們可以這麼定義dp:

`dp[i][j]: the minimum path sum at i-th row and j-th column`

由於對於dp[i][j]來說，他可以從dp[i-1][j']轉移過來，其中`j'`為不與`j`相同column的任意grid
因此我們就三層循環，外面兩層遍歷`i`, `j`, 最裡面遍歷`j'`即可

狀態轉移如下, 最終答案就是在`n-1` row 裡挑最小的path sum

```py
for i in range(1, n):
    for j in range(n):
        for prev in range(n):
            if prev == j: continue
            dp[i][j] = min(dp[i][j], dp[i-1][prev] + grid[i][j])
return min(dp[n-1])
```

由於`i=0`時dp[i-1]會越界，所以我們把i=0的結果單獨處理
```py
dp = [[0] * n for _ in range(n)]
for j in range(n):
    dp[0][j] = grid[0][j]
```

**Optimized**

但這樣會TLE, 觀察一下會發現其實對於i-th row來說
dp[i]肯定是從`i-1` row中最小的dp[i-1]轉移過來，只要不在同一column
如果min(dp[i-1])也在`j` column的話，那就是從次小的dp[i-1][j']轉移過來

所以對於dp[i][j]來說，他肯定是從dp[i-1]中最小或次小的path sum轉移過來
所以我們可以把這結果提前算出來然後共用，減少運算次數

我們提前找出dp[i-1]裡的最小值跟次小值
然後對於dp[i][j]來說，他肯定是從這兩個其中一個狀態轉移過來
```py
for i in range(1, n):
    prevMin = []
    for prev in range(n):
        prevMin.append([dp[i-1][prev], prev])
    prevMin.sort()
    
    for j in range(n):
        if prevMin[0][1] != j:
            dp[i][j] = prevMin[0][0] + grid[i][j]
        elif len(prevMin) > 1 and prevMin[1][1] != j:
            dp[i][j] = prevMin[1][0] + grid[i][j]
```