# Intuition

有點像knapsack dp problem
對於i-th wall, 我們可以選擇給paid painter或是free painter

- 如果給paid painter: dfs(i+1, paid_time+time[i])
- 如果給free painter: dfs(i+1, paid_time-1)

**base case**

當畫完每一面牆後 (i==n):
    - 如果paid_time >= 0, 代表合法解
    - 如果paid_time < 0, 代表有free painter在不夠paid_time的情況下畫畫, 不合法解

再來還有一點是, `當i+paid_time >= n`時, 這代表還後面[i+1, n-1]這段範圍都可以給free painter處理
這時直接返回`0` cost即可

# Other Solution - bottom-up

想當然也可以bottom-up
一樣想成是knapsack problem

對於這些paid painter來說, 我們可以把它分配給任意i-th wall或是不採用

我們定義dp[i][j]: the minimum cost for using first i paid painter to finish j walls

那麼對於painter[i]來說, 如果他是畫j-th wall, 那麼他的前驅狀態會是上一輪的`j-time[i]-1`

原因是他畫了j-th wall: 畫了一面牆
並且在time[i]的過程中, free painter會畫time[i]面牆
所以在上個狀態我們已經畫了`j-time[i]-1`面牆

```
X X X X X X [{X X X X X} X]
               time[i]   j
```
因此`dp[i][j] = dp[i-1][j-time[i]-1] + cost`

但我們也可以不選painter[i]
所以我們就是取`min(dp[i-1][j], dp[i-1][j-time[i]-1] + cost)`

因此整個框架是:
對於第i個畫家來說, 選擇來畫第j面牆 (1-indexed, 總共n面牆)
```py
dp = [[inf]*(n+1) for _ in range(n)]
for i, (c, t) in enumerate(zip(cost, time)):
    for j in range(1, n+1):
        dp[i][j] = min(dp[i-1][j], dp[i-1][max(0, j-t-1)]+c)
```

那最終答案就是`dp[n-1][n]`, 考慮全部畫家來畫完n面牆

**base case**

0面牆的話不管有多少painter, cost都是0
```py
for i in range(n):
    dp[i][0] = 0
```