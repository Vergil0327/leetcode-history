# Intuition

可能情況:

```py
m, n = len(grid), len(grid[0])
```

m:even
n:odd
X X X X
X X X X
X X X X

m:even
n:even
X X X X
X X X X
X X X X
X X X X

m:odd
n:odd
X X X
X X X
X X X

m:odd
n:even
X X X
X X X
X X X
X X X

首先最低操作數算法為:

```py
step = 0
for i in range(m//2):
    for j in range(n//2):
        # palindrome => 4 points should be equal
        a = grid[i][j]
        b = grid[i][n-1-j]
        c = grid[m-1-i][j]
        d = grid[m-1-i][n-1-j]

        one_cnt = a+b+c+d
        step += min(one_cnt, 4-one_cnt) # (全轉成0, 全轉成1)
```

四個位置為一組, 只可能是(0,0,0,0)或(1,1,1,1)

令m, n = len(grid), len(grid[0])

當m, n都是偶數時: 可直接返回最低操作數`step`
但只要m, n有任一不為偶數, 就就會有額外的中間那行(或列)需要考慮palindrome

1. n%2 == 1:

```py
ones = diff_pair = 0
for i in range(m//2):
    a, b = grid[i][n//2], grid[m-1-i][n//2]
    ones += a+b
    diff_pair += int(a != b)
```

2. m%2 == 1:

```py
ones = diff_pair = 0
for j in range(n//2):
    a, b = grid[m//2][j], grid[m//2][n-1-j]
    ones += a+b
    diff_pair += int(a != b)
```

3. m%2 and n%2: 正中央的元素必須為0

例如一個3x3的grid, 對於grid[i][j]來說, 四個四個為一組
然後再考慮中間那行(跟列)後, 也都是要麻四個`1`或四個`0`
如果正中央元素不為0, 那麼最後1的組合必定不被4整除

```
X O X
O 1 O
X O X
```

所以如果`m%2 and n%2`, step += (1 if centered element == 1 else 0)

所以我們整個考慮完palindrome後, 操作數為`step + diff_pair`

這時在注意一下, 因為diff_pair這邊是兩個兩個相對應, 所以diff_pair這邊: one%4 = 0 or 2
diff_pair相當於(1,0) pair的個數, 這時有兩種情況:

1. 奇數個(1,0) pair: 部分pair轉成(0,0)後也會被4整除
2. 偶數個(1,0) pair: 轉成(1,1)後必定被4整除

唯一的會使one%4 != 0的情況為: **0個(1,0) pair**, 這時`one%4 == 2`
這情況我們勢必得花兩個額外步驟使(1,1)變為(0,0) 或是 (0,0)轉為(1,1)
所以當diff_pair這邊只存在(1,1) pair, 亦即`diff_pair == 0`且`one%4 > 0`時, 需要額外多兩步

所以整理一下就是:

```py
m, n = len(grid), len(grid[0])

step = 0
for i in range(m//2):
    for j in range(n//2):
        # palindrome => 4 points should be equal
        a = grid[i][j]
        b = grid[i][n-1-j]
        c = grid[m-1-i][j]
        d = grid[m-1-i][n-1-j]

        one_cnt = a+b+c+d
        step += min(one_cnt, 4-one_cnt) # (全轉成0, 全轉成1)

ones = diff_pair = 0
if n%2 == 1: # column為奇數
    for i in range(m//2):
        a, b = grid[i][n//2], grid[m-1-i][n//2]
        ones += a+b
        diff_pair += int(a != b)

if m%2 == 1: # row為奇數
    for j in range(n//2):
        a, b = grid[m//2][j], grid[m//2][n-1-j]
        ones += a+b
        diff_pair += int(a != b)

if m%2 and n%2: # 正中央元素
    step += grid[m//2][n//2]

if diff_pair == 0 and ones%4 > 0: # 奇數個(1,1) pair
    step += 2

return step+diff_pair
```