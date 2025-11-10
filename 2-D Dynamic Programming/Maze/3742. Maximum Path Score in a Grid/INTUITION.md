# Intuition

一開始是想要用dijkstra去找max score, 但後來發現我們不能單純以score大小來判斷

因為以這兩這例子為例:
- Path A: score=5, cost=3
- Path B: score=4, cost=2

較低score那邊也可能最後成為較高score的路徑(因為cost更低, 也許能走更多格子)

所以這情況告訴我們, 我們應該遍歷所有可能情形來找出row=m-1, col=n-1, cost<=k時的max score
=> dynamic programming

一但想到dp就簡單了, 狀態變化相當直覺, 每個(row,column)遍歷可能cost並更新dp狀態:

```py
# to bottom
for kk in range(k+1):
    new_cost = kk+int(grid[r+1][c] > 0)
    dp[r+1][c][new_cost] = max(dp[r+1][c][new_cost], dp[r][c][kk] + grid[r+1][c])

# to right
for kk in range(k+1):
    new_cost = kk+int(grid[r][c+1] > 0)
    dp[r][c+1][new_cost] = max(dp[r][c+1][new_cost], dp[r][c][kk] + grid[r][c+1])
```