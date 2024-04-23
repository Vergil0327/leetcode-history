# Intuition

從例子上來看, 得從全局最小的格子出發, 由小到大依序處理
每次都能決定與該格子同row & col的其他格子, 由小到大持續將rank += 1

```
Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

[[20,-21,14]
 [-19,4,19]
 [22,-47,24]
 [-19,4,19]]

 [[4,2,3]
  [1,3,4]
  [5,1,6]
  [1,3,4]]

-47
[[0,2,0]
 [0,3,0]
 [2,1,3]
 [0,3,0]]

-21
[[4,2,3]
 [0,3,0]
 [2,1,3]
 [0,3,0]]

-19
[[4,2,3]
 [1,3,4]
 [2,1,3]
 [1,3,4]]

 4
 [[4,2,3]
  [1,3,4]
  [2,1,3]
  [1,3,4]]

  ...

  22
  [[4,2,3]
   [1,3,4]
   [5,1,6]
   [1,3,4]]
```

看上面例子, 從全局最小的格子出發, 由小到大依序處理
每次都能決定與該格子同row & col的其他格子
=> 也就是由小到大持續將rank += max(max(row), max(cell)) + 1
=> 但如果值相等的話, 則無須+1, 例如:

Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]

這樣問題就變成得高效求出該cell的max(max(row), max(col))

當時卡在這想法想不出突破口
但其實這邊我們應當將該cell的row, col看成同個group, 然後去找出他們的max(group)
既然是要將row跟col併成一塊, 那代表可以試著思考union-find

這邊要注意的是, 前面有觀察到值相同rank無需+1, 但其實更近一步去想的話
在同個row或col上如果有數值相同的格子的話, 他們rank應當是相同的, 代表我們應當視作同一個格一併處理
所以我們row跟col都得先遍歷一遍, 找出來然後透過union-find併作一塊

```py
m, n = len(matrix), len(matrix[0])
parent = list(range(m*n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return
    if px <= py:
        parent[py] = px
    else:
        parent[px] = py

for i in range(m):
    tmp = [(matrix[i][j], i*n+j)for j in range(n)]
    tmp.sort()

    for j in range(1, n):
        if tmp[j-1][0] == tmp[j][0]:
            union(tmp[j-1][1], tmp[j][1])

for j in range(n):
    tmp = [(matrix[i][j], i*n+j) for i in range(m)]
    tmp.sort()

    for i in range(1, m):
        if tmp[i-1][0] == tmp[i][0]:
            union(tmp[i-1][1], tmp[i][1])
```

然後把同個group的值都給並在一塊

```py
group = defaultdict(list)
for i in range(m):
    for j in range(n):
        p = i*n + j
        group[find(p)].append(p)
```

最後就全局由小到大依序找出rank

```py
arr = sorted([(matrix[i][j], i*n+j, i, j) for i in range(m) for j in range(n)])

res = [[0]*n for _ in range(m)]
rowRank = [0]*m # row[i]: max rank in i-th row
colRank = [0]*n # col[i]: max rank in i-th col

for _, p, r, c in arr:
    rank = 0
    for member in group[find(p)]:
        row, col = member//n, member%n
        rank = max(rank, rowRank[row])
        rank = max(rank, colRank[col])

    for member in group[find(p)]:
        row, col = member//n, member%n
        res[row][col] = rank+1

        # update back rowRank & colRank
        rowRank[row] = rank+1
        colRank[col] = rank+1
return res
```

但這時會發現, 我們在更新rank的時候, 會連member一同更新, 但member有可能之後還會再遍歷到, 然後又反覆更新一次
例如. matrix = [[7,7],[7,7]], Output=[[1,1],[1,1]]
但我們會重複四次而變[[4,4],[4,4]]

所以有個重點是: 我們已經全局由小到大更新rank, 相同值如前面所說應該視為一個數並一起更新, 所以我們應該要避免重複更新 => 只更新一次

最後那段記得加上:

```py
for _, p, r, c in arr:
    if res[r][c] > 0: continue # <---- avoid multiple update

    rank = 0
    for member in group[find(p)]:
        row, col = member//n, member%n
        rank = max(rank, rowRank[row])
        rank = max(rank, colRank[col])

    for member in group[find(p)]:
        row, col = member//n, member%n
        res[row][col] = rank+1

        # update back rowRank & colRank
        rowRank[row] = rank+1
        colRank[col] = rank+1
return res
```