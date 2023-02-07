# Intuition

那既然如此，放越多間，間隔越短
放越少間，間隔就越長，這樣的單調特性可以試著用二分搜值來猜出答案

那判斷我們猜的對不對的方式可以透過:
假如二分搜值猜的值為`D`，那對於每段間隔，我們會需要放置`ceil(abs(stations[i]-stations[i+1])/D)-1`這的多間
這樣我們就可以求得當下猜的符不符合答案

```py
k = 0
for i in range(len(stations)-1):
    k += ceil(abs(stations[i]-stations[i+1])/D)-1

return k <= K
```

那由於求的是一個誤差範圍小於$10^{-6}$的D，因此這邊的二分搜值要稍微改一下
```py
l, r = 0, 1e8
while r-l < 1e-6>:
    mid = l + (r-l)/2
    if check(mid):
        r = mid
    else:
        l = mid
return l
```