# Intuition

首先這題肯定有解，最糟情況就是一個長度為0的矩陣，那對長邊就會是`min(ROWS, COLS)`

再來就是我們要求的這個maximum side length，他有個極值存在，越長則符合條件的矩形越少，越短則越多

因此我們可以試試binary search來猜這個value
那麼我們的search space就是`[0, min(ROWS, COLS)]`

那再來就是要解決如何判斷長度為`mid`的square存不存在

最簡單的方式就是我們可以把每一列處理成prefix sum
這樣我們就能用`O(ROWS*COLS*LENGTH)`的時間複雜度
來判斷，核心的binary search by value則為

```py
l, r = 0, min(ROWS, COLS)
while l < r:
    mid = r - (r-l)//2
    if squareExists(mid):
        l = mid
    else:
        r = mid-1
return l
```

- time complexity

O(ROWS*COLS*LENGTH*log(min(ROWS, COLS)))

# Optimized

或者我們可以進一步利用排容原理，架構出2D prefix sum來更快速的判斷square存不存在

2D prefix sum就是對於每個點我們累加上方一格，及左方一格，然後再減去左上那格
這是因為我們會累加行跟列的prefix sum，因此左上會重複加到，所以要扣掉

```py
presum2D = [[0]*(COLS+1) for _ in range(ROWS+1)]
for r in range(1, ROWS+1):
    for c in range(1, COLS+1):
        # presum[r][c] = 左 + 上 - 左上 + 當前這格
        presum2D[r][c] = presum2D[r-1][c] + presum2D[r][c-1] - presum2D[r-1][c-1] + mat[r-1][c-1]
```

再來判斷一個2D矩形的加總一樣是透過排容原理
如果舉行的左上角為(r,c)右下角為(r+len, c+len)
那麼矩形的和就會如下所示
```py
for r in range(ROWS-maxLen+1):
    for c in range(COLS-maxLen+1):
        SUM = presum2D[r+maxLen][c+maxLen]+presum2D[r][c]-presum2D[r+maxLen][c]-presum2D[r][c+maxLen]
```


如此一來，時間複雜度可以進一步減少至
O(ROWS*COLS*log(min(ROWS, COLS)))