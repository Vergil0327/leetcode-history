# Intuition

想知道有多少方法能產生兩個數之間的所有符合條件的數 => digit DP
我們可以直接拿出我們的digit DP模板出來

```py
low, high = str(start), str(finish)
while len(low) < len(high):
    low = "0" + low
    
n = len(low)

@cache
def dfs(i, leading, lowerThanHigh, higherThanLow):
    if i == n: return 1

    start = 0 if higherThanLow else int(low[i])
    end = 10 if lowerThanHigh else int(high[i])+1

    res = 0
    for d in range(start, end):            
        res += dfs(i+1,
                    leading and d == 0,
                    lowerThanHigh or d < int(high[i]),
                    higherThanLow or d > int(low[i]))
    return res
return dfs(0, True, False, False)
```

再來就是如何適當地將合法條件加入到dfs裡面來減少dfs的分支
首先比較明顯的是我們的digit只能是[0,limit], 所以我們的end必須再加上一個`min(end, limit+1)`

```py
def dfs(i, leading, lowerThanHigh, higherThanLow):
    if i == n: return 1

    start = 0 if higherThanLow else int(low[i])
    end = 10 if lowerThanHigh else int(high[i])+1
    end = min(end, limit+1) # <--- here

    res = 0
    for d in range(start, end):            
        res += dfs(i+1,
                    leading and d == 0,
                    lowerThanHigh or d < int(high[i]),
                    higherThanLow or d > int(low[i]))
    return res
```


再來是最重要的合法條件: **suffix == s**
也就是當我們的`i >= n-m`時, 從這之後開始的每個位置都必須等於相對應的s[j]
從`i >= n-m`開始, 這之後的所有digit都只有一種可能, 其他都是非法的我們可以直接skip掉, 所以我們可以加上

```py
def dfs(i, leading, lowerThanHigh, higherThanLow):
    if i == n: return 1

    start = 0 if higherThanLow else int(low[i])
    end = 10 if lowerThanHigh else int(high[i])+1

    res = 0
    for d in range(start, end):            
        if i >= n-m and str(d) != s[i-(n-m)]: continue # <--- here
        res += dfs(i+1,
                    leading and d == 0,
                    lowerThanHigh or d < int(high[i]),
                    higherThanLow or d > int(low[i]))
    return res
```

最終答案就是`dfs(0, True, False, False)`