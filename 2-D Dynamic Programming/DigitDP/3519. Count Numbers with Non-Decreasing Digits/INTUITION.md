# Intuition

概念上就是經典的digit DP, 首先看digit DP模板:

```py
def dfs(i, greaterThanLow, lowerThanHigh, leadingZero, prev):
    if i >= n: return 1 # one valid string
    
    start = 0 if greaterThanLow else int(LOW[i])
    end = b if lowerThanHigh else int(HIGH[i])+1

    res = 0
    for d in range(start, end):
        if d < prev: continue # for non-decreasing

        res += dfs(i+1,
                   greaterThanLow or d > int(LOW[i]),
                   lowerThanHigh or d < int(HIGH[i]),
                   leadingZero and d == 0,
                   d)
        res %= mod
    return res
```

我們只需要將一開始的`l`, `r`轉換成`b`進制後, 即可得到`LOW`, `HIGH`
剩下就套入模板, 計算看範圍內能組出多少合法digits即可