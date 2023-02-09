# Intuition

首先從第一個例子來看，假如我們minimum require force越大，代表間隔就會越大，在一定範圍內能放的球就越少
反之如果force越小，球就能放得更密集，就能放得越多
這樣的性質聽起來可以試著用binary search來猜require force，找出極值

這時我們再依據條件來放球，只有當|x-y| >= require force才能放

```
force = 3
1,2,3,4,5,6,7
o     o     o

force = 4
1,2,3,4,5,6,7
o       o    
```

我們可以以greedy的方式，只要一滿足 |x-y| >= force 我們就放球，盡可能地放
如果可以放滿`m`個的話，代表這時猜測的force為可行解，然後我們再繼續往小裡猜

binary search 核心框架如下:
由於force定義為|x-y|，最小至少為`1`，最遠則為nums裡的最大值減去最小值
search space 為`[1, max(position)-min(position)]`

```py
l, r = 1, max(position) # 或者最大值取個大概即可，binary search對數級別減少，效率很高沒太大差異
while l < r:
    mid = r - (r-l)//2
    if canUseEveryBall(mid):
        l = mid
    else:
        r = mid-1
return l
```

# Complexity

- time complexity
$$O(nlogn + nlog(max(position)))$$

- space complexity
$$O(1)$$