# Intuition

```
queries = [(0,0,2,2), (1,1,3,3)]

1   0   1   -1  0
0   1'  0   1'  0
1   0   1   0   0
0   1'  0   1'  0
0   0   0   0   0
```

M = len(matrix)
我們可以把matrix想成有M個difference array

當只有一維array時，我們可以透過標記起點與終點來達到O(n)時間加總所有計算
例如如果我們要讓 index [0,3], [2,6] 全部區間加1的話，我們可以透過在`index=0, 2的位置+= 1`，然後在`index=3, 6的後一個位置-=1`
ex. nums = [1,0,1,0,-1,0,0,-1,0]
這樣我們就可以用O(n)的時間，透過 nums[i] += nums[i-1]來得到我們要的以O(n)時間達到多個 range update

因此我們把matrix想成多個difference array後，對於每個query:
- 在每個ROW標記 +=1
- 在COL+1的位置標記 -= 1

```
for r1,c1,r2,c2 in queries:
    for r in range(r1, r2+1):
        mat[r][c1] += 1
        if c2+1 < n:
            mat[r][c2+1] -= 1
```

最後在透過O(N * N)的時間一次更新即可

# Complexity

- time complexity
$$O(len(queries) * N + N*N)$$

- space complexity

$$O(N^2)$$

# Optimized

但這題有個更好的2D差分數組的解法

我們可以觀察這四格

```
(row1, col1)  (row1, col2)
X ... ... ... ... ... ..X
X ... ... ... ... ... ..X
X ... ... ... ... ... ..X
(row2, col1)  (row2, col2)
```
如果我們要在左上為(row1, col1)，右下為(row2, col2的範圍矩陣做range addition的話
首先我們要做的，就是標記差分的位置，並在之後透過透過排容原理進行更新，標記位置分別是:
1. (row1, col1)的位置標記 += 1
2. (row1, col2+1)的位置標記 -= 1
3. (row2+1, col1)的位置標記 -= 1
4. (row2+1, col2+1)的位置標記 += 1

```py
# Principle of inclusion and exclusion 排容原理
diff2D = [[0] * (n+1) for _ in range(n+1)]
for r1, c1, r2, c2 in queries:
    diff2D[r1][c1] += 1     # top-left
    diff2D[r1][c2+1] -= 1   # right-portion
    diff2D[r2+1][c1] -= 1   # bottom-portion
    diff2D[r2+1][c2+1] += 1 # bottom-right
```

之所以要在這四個點標記是因為，我們在進行更新的時候他們會分別代表加總的開始與結束位置
範圍更新有兩種:
1. 第一種方式是:
   1. 先對每一 ROW 掃過一次，進行diff array的更新
   2. 然後再對 COL 方向掃過一次，進行diff array的更新

        ```py
        # method 1, sweepline on rows then sweepline on cols
        for i in range(1, n+1):
            for j in range(n+1):
                diff2D[i][j] = diff2D[i][j] + diff2D[i-1][j]
        for i in range(n+1):
            for j in range(1, n+1):
                diff2D[i][j] = diff2D[i][j] + diff2D[i][j-1]
        ```
    會發現我們前面標記的四個點，正好就是ROW方向的起始與結束以及COL方向的起始與結束
    而在進行第二次COL方向時，其實也就是將一維的矩陣疊加拓展到二維矩陣的更新

2. 第二種方式則是一次性透過排容原理疊加

    ```py
    # method 2
    result[0][0] = diff2D[0][0]
    for i in range(n):
        for j in range(n):
            top = result[i-1][j] if i-1 >=0 else 0
            left = result[i][j-1] if j-1 >= 0 else 0
            topleft = result[i-1][j-1] if i-1 >=0 and j-1 >=0 else 0
            result[i][j] = top + left - topleft + diff2D[i][j]
    ```

這邊我們最好用作圖比較好理解，並從最左上位置觀察開始進行更新時發生什麼事

```
matrix如下:

(row1, col1) (row1, col2) ...
(row2, col1) (row2, col2) ...
```
首先看到如果我們要更新`(row2, col2)`的差分更新時：

加上的`top=result[row1][col2]`這部分，其實是row1這整行的更新結果，有點像是 prefix diff array，包含了水平方向矩陣`(row1, col1) ... (row1, col2)`

而下一個加上的`left=result[row2][col1]`則包含了垂直方向矩陣`(row1, col1) ... (row2, col1)`

因此會重複疊加更新到`(row1, col1)`這格，所以我們必須再扣掉`topleft=result[row1][col1]`

最後再加上`(row2, col2)`自身的差分 diff2D[row2][col2]即完成了累積至右下為`(row2, col2)`矩陣範圍的差分更新