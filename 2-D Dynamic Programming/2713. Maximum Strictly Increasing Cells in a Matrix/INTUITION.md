# Intuition

這題當初比較直覺想到的是top-down的方式
但這樣大致上會是個O(mn*(m+n))的時間複雜度, 會超時
整整四十分鐘就卡在這裡

```py
def maxIncreasingCells(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])

    ROWS = defaultdict(set)
    COLS = defaultdict(set)
    for i in range(m):
        for j in range(n):
            ROWS[i].add((mat[i][j], j))
            COLS[j].add((mat[i][j], i))
            
    @lru_cache(None)
    def dfs(i, j):
        res = 0
        for nei in ROWS[i]:
            v, jj = nei
            if v > mat[i][j]:
                res = max(res, dfs(i, jj) + 1)

        for nei in COLS[j]:
            v, ii = nei
            if v > mat[i][j]:
                res = max(res, dfs(ii, j) + 1)
        return res
            
    
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))
    return res+1
```

但既然top-down方式有了
我們應該也能反過來看看bottom-up的方式是不是有能優化的地方

首先由於我們是要在這個`m x n`的矩陣裡找出找最長路徑

我們先用一個hashmap紀錄每個值所對應的位置`(i,j)`後, 最關鍵的突破口是我們將全部的值**由大到小排序**
因為我們是bottom-up的方式, 所以我們從最大的值一步一步往回找回來
當找完當前最大的值的長度後, 再看有沒有下個次大的能接在後面

```py
m, n = len(mat), len(mat[0])

positions = defaultdict(list)
for i in range(m):
    for j in range(n):
        positions[mat[i][j]].append((i, j))

for key in sorted(positions, key=lambda x:-x): # 由大到小
    # find longest increasing path
```

所以我們在這定義`dp[i][j]`: the longest path ended at grid[i][j]

那麼dp[i][j]的前驅狀態則有兩個:
- 從row方向跳過來
- 從column方向跳過來

所以我們還需要紀錄`rowPath`跟`colPath`
rowPath[r]: 代表在`r`這一行上的最長路徑
colPath[c]: 代表在`c`這一行上的最長路徑

那麼dp[i][j]就是從這兩者取較大的轉移過來並且+1
=> `dp[i][j] = max(rowPath[row], colPath[col])+1`

在更新完dp後記得再返回去更新當前的rowPath以及colPath

```py
dp = [[0] * n for _ in range(m)]
rowPath = defaultdict(int)
colPath = defaultdict(int)

res = 0
for key in sorted(positions, key=lambda x:-x): # 由大到小
    for row, col in positions[key]:
        dp[row][col] = max(rowPath[row], colPath[col])+1
        res = max(res, dp[row][col])

    for row, col in positions[key]:
        rowPath[row] = max(rowPath[row], dp[row][col])
        colPath[col] = max(colPath[col], dp[row][col])
return res
```

最終答案就是從所有位置裡取最大的

可以從dp[row][col]裡取也可以從rowPath和colPath裡取
但這邊我們同步更新全局最大`res`即可

所以本題突破口就是以bottom-up的方式並**排序**
這樣我們就能重複利用之前計算過的結果

# Complexity

- time complexity
$$O(mnlog(mn))$$

- space complexity
$$O(mn)$$