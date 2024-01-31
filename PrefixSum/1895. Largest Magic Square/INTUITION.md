# Intuition

這題想了一下brute force後會很快發現, 其實就是以左上角為特徵位置
遍歷可能的square length長度後, 高效找出每一個row, column, 以及兩個對角線的和

那其實就是需要這四個方向的prefix sum

困難點就是小心越界以及對角線這兩個方向的prefix sum即可

```py
m, n = len(grid), len(grid[0])
rowsum = [[0]*(n+1) for _ in range(m+1)]
colsum = [[0]*(n+1) for _ in range(m+1)]
diag1 = [[0]*(n+2) for _ in range(m+2)]
diag2 = [[0]*(n+2) for _ in range(m+2)]
for i in range(1, m+1):
    for j in range(1, n+1):
        rowsum[i][j] = rowsum[i][j-1] + grid[i-1][j-1]
        colsum[i][j] = colsum[i-1][j] + grid[i-1][j-1]
        diag1[i][j] = diag1[i-1][j-1] + grid[i-1][j-1]
        diag2[i][j] = diag2[i-1][j+1] + grid[i-1][j-1]
```

每一格都是合法magic square, 所以**res至少是1**
那接下來我們用1-indexed遍歷, 找出合法magic square
由於我們是1-indexed, 更新res時記得是`res = max(res, length+1)`

```py
res = 1
for i in range(1, m+1):
    for j in range(1, n+1):
        for length in range(min(m-i, n-j), 0, -1):
            SET = set()
            SET.add(diag1[i+length][j+length] - diag1[i-1][j-1])
            SET.add(diag2[i+length][j] - diag2[i-1][j+length+1])
            for l in range(length+1):
                SET.add(rowsum[i+l][j+length] - rowsum[i+l][j-1])
                SET.add(colsum[i+length][j+l] - colsum[i-1][j+l])
            if len(SET) == 1:
                res = max(res, length+1)
return res
```