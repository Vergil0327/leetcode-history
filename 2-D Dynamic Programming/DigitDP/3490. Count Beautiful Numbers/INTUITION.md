# Intuition

看到`1 <= l, r <= 10^9`, 單純O(n)可能就行不通了
但如果看他們的**位數**, 那頂多就9個位數, 而且裡面的判斷又跟digits有關

所以馬上就想到經典的digit dp問題

套用digit DP模板:

這邊只要維護好我們兩個用來判斷是否為合法digit string得兩個狀態: product跟total即可

> product: 注意別將leading zero的0也給乘進去, 否則會重複計算"020"跟"20"

```py
low, high = str(l), str(r)
while len(low) < len(high):
    low = "0" + low

n = len(high)

@cache
def dfs(i, leadingZero, isGreaterThanLow, isLowerThanHigh, prod, total):
    if i >= n: return int(prod%total == 0)

    start = 0 if isGreaterThanLow else int(low[i])
    end = 10 if isLowerThanHigh else int(high[i])+1

    res = 0
    for d in range(start, end):
        p = prod * d if d > 0 or not leadingZero else prod
        res += dfs(i+1,
                   leadingZero and d == 0,
                   isGreaterThanLow or d > int(low[i]),
                   isLowerThanHigh or d < int(high[i]),
                   p,
                   total+d)
    return res
```