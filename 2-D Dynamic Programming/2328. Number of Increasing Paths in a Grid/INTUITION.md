# Intuition

一開始觀察是

如果定義dp[i][j]: the number of strictly increasing paths to reach grid[i][j]
一開始dp[i][j]都是1

再來由於要strictly increasing path, 我們得由小到大累加path
只要當周圍四格的值`grid[i'][j']`大於`grid[i][j]`, 我們就能進行狀態轉移
`dp[i'][j'] += dp[i][j] if grid[i'][j] > grid[i][j]`

```
ex1.
1 1
3 4

initial state:
1 1 -> 1 1 -> 1 1 -> 1 1
1 1 -> 2 1 -> 2 2 -> 2 4
(0,0) (0,1)  (1,0)  (1,1)

1 3
4 1

1 1 -> 1 2 -> 1 3
1 1 -> 2 1 -> 3 1
(0,0) (1,1)   (0,1)
```

所以想法是先用minHeap排序
然後依據grid[i][j]由小到大更新dp[i][j]
那最後答案就是sum(dp[i][j])

time: mnlog(mn)

# Optimization

但其實我們不需要排序
我們可以每個grid[i][j]位置進行DFS並把每個位置能走的path長度記錄下來

定義dfs(r,c)返回的是從grid[i][j]開始走, 能湊成strictly increasing path的方法數
再配合memorization避免重複計算即可

整個high level的架構如下
```py
res = 0
for r in range(m):
    for c in range(n):
        res += dfs(r, c)
        res %= mod
return res
```

