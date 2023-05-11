# Intuition

這類型要先想辦法找出該幾何形狀的特徵值, ex. leetcode 221. 就找每個位置的最長邊, 然後考慮對角以及相鄰兩點
這題的金字塔也是一樣:
```
X X X X O X X X X X
X X X O O O X X X X
X X O O O O O X X X
```

- 對於一個金字塔, 可看出他的層數跟他的底座長度息息相關. 對於一個兩層金字塔(h=2), 底座至少也要有半徑為h的合法長度
- 再來如果他有一個半徑為h的底座, 以正金字塔來說, 他的上一層必須至少有`h-1`層, 代表底座半徑必須至少為`h-1`

因此如果定義`dp[i][j]`為: **the maximum radius/height for current grid[i][j] as middle point of bottom layer**
- 如果這個底座可以組成一個3層金字塔, 那他肯定也能組成一個2層金字塔, 並且不同中點位置的底座所形成的金字塔不會互相重疊
  - 代表特徵值不會重複計算
  - 如果他能組成`dp[i][j]=3`, 亦即3層的金字塔, 那代表他對總金字塔個數的貢獻為**2** (1個2層金字塔跟1個3層金字塔)

因此首先我們可以先計算對於每個點作為底座終點來說, 他左半徑以及右半徑最長為多少, 取`min()`即可知道他最多能作為幾層金字塔的底座

```py
m, n = len(grid), len(grid[0])
for i in range(m):
    cnt = 0
    for j in range(n):
        if grid[i][j] == 1:
            cnt += 1
        else:
            cnt = 0
        left[i][j] = cnt

for i in range(m):
    cnt = 0
    for j in range(n-1, -1, -1):
        if grid[i][j] == 1:
            cnt += 1
        else:
            cnt = 0
        right[i][j] = cnt
```

再來計算每個點的`dp[i][j]`, 我們用`dp[i][j]`來儲存正金字塔的個數, `dpInv[i][j]`來儲存倒金字塔的個數
正金字塔從`rows=0`往下計算, 倒金字塔則從`rows=m-1`開始計算
```py
res = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0: continue

        if i == 0:
            dp[i][j] = 1
        else:
            h = min(left[i][j], right[i][j]) # or radius
            dp[i][j] = min(h, dp[i-1][j]+1)
            res += dp[i][j]-1
```


