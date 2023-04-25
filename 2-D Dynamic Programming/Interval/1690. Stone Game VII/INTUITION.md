# 2-D DP - 區間型DP

## Intuition

### DP Definition

首先定義dp[i][j]為`當區間為stones[i:j]的最大得分差(the maximum difference when playing in stones[i:j])`

先解決小區間，再解決大區間
所以外層循環length從小到大，length=1,2視為special case單獨處理

對於一個`stones`數組(陣列)來說:
1. 如果我們取走第i個(left-most)，那麼得分為`sum[i+1:j]`
   - 而下一回合對手的得分差`dp[i+1][j]`
   - 因此這回合的最大得分差為`sum[i+1:j]-dp[i+1][j]`
2. 如果我們取走第j個(right-most)，那麼得分為`sum[i:j-1]`
   - 而下一回合對手的得分差`dp[i][j-1]`
   - 因此這回合的最大得分差為兩者相減，`sum[i:j-1]-dp[i][j-1]`
3. 前兩者取最大值即為dp[i][j]

如下圖所示
```
          X [X X X X X X X X X]
choose i: i i+1              j
dp[i][j] = sum(stones[i+1:j]) - dp[i+1][j] = current Alice score - bob's difference in next round = alice's difference

          [X X X X X X X X X] X
choose j:  i               j-1 j
dp[i][j] = sum(stones[i:j-1]) - dp[i][j-1]
```

### Base Case

- 當長度為1時:

ex. stones=[1]
取走後得分為0

- 當長度為2時:

ex. stones[a, b]

取走a，得分為b
取走b，得分為a
因此最大得分為兩者取最大值`max(a, b)`

### Prefix Sum

既然我們需要區間和，那麼我們可以預先計算prefix sum
然後注意更新DP的同時，小心index不要越界
ex. sum(stones[i+1:j]) 由於i+1可能越界
因此我們`區間和 = presum[min(j+1, n)]-presum[i+1]`，對index與總長度取max