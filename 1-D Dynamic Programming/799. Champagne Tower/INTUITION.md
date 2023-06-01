# Intuition

```
  1
 1 1
1 1 1
```

先觀察一下香檳塔, 會發現每一個杯子都是由上一層的兩個杯子所溢出的香檳的加總
寫成數學形式的話, 大概會是:

```
tower[i][j] = overflow(tower[i-1][j-1]) + overflow(tower[i-1][j])
```

如果定義`dp[i][j] = how full of glass at i-th row and j-th column`的話
對於當前的dp[i][j]來說, dp[i-1][j]跟dp[i-1][j-1]並沒有溢出多少的私訊
所以沒辦法透過這兩個狀態來更新dp[i][j]

但dp還有另一種比較少用的寫法是, 用現在的狀態更新未來的狀態
那這就好理解多了, 也很符合這個倒香檳的情境

首先對於當前來說, 可想成一開始我們有一個杯子裝了`poured`這麼多的香檳
`currRow = [poured]`

那麼對於下一層來說, 每一杯都會收到前一層左右兩杯溢出的一半香檳
以兩層來說, 如果第一層倒了兩杯, 那麼就是溢出一杯的量
底下就各分0.5
```
   1 (+ 1 excess)
0.5 0.5
```

所以這時dp狀態就出來了
並且由於每一層只跟上一層有關, 所以我們用兩個array來表達即可
並且更新完nextRow後, 因為溢出的部分已經分配完
記得把當前row[j]重新更新為1

```
excess = currRow[j]-1
nextRow[j] = excess/2
nextRow[j+1] = excess/2

row[j] = 1
```

然後我們看`excess = currRow[j]-1`這個部分可能為負值
這是因為如果上層已經倒不滿了, 所以我們這個表達式只適用`excess >= 0`

因此我們整個狀態更新可寫成

```py
currRow = [poured]
nextRow = []
for i in range(query_row+1):
    nextRow = [0]*(i+2)
    for j in range(i+1):
        if currRow[j] >= 1: # if it's overflow
            nextRow[j] += (currRow[j]-1)/2
            nextRow[j+1] += (currRow[j]-1)/2
            currRow[j] = 1
    row, nextRow = nextRow, row
```

最後跳出時, 由於我們`row`跟`nextRow`會掉換
所以最終結果存在`nextRow`裡
最終返回`nextRow[query_glass]`即可