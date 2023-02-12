# Intuition

首先我們看一下，如果k=5，我們能涵蓋的就是startPos正負5的區間
但要注意的是折返點，我們可以發現其實最多就折返一次，然後`折返的距離*2+另一邊的距離<=k`

```
k = 5
<<<<<
 <<<<>
   <<>
     >>>>>
    <>>>>
    <>>
```

如果是 `x ... startPos ... y`的話，會有以下的限制:
1. 先往左再往右: 2*(startPos-x) + (y-startPos) <= k
2. 先往右再往左: 2*(y-startPos) + (startPos-x) <= k

也就是當y往右移動的時候，x也會因為限制而往左移動
同樣地，x往左移動的時候，y也會跟著往右移動
這代表可以對這兩種情形進行討論然後用sliding window來找出最佳解

1. 先往左再折返往右的情形

先找出右邊界 `r`: `r = bisect.bisect_left(axis, startPos)`
再來r持續往右走，當 `2*l + r > k` 的時候，代表要移動左邊界了

```py
while axis[l] <= startPos and (axis[r]-startPos) + 2 * (startPos-axis[l]) > k:
    l += 1
```

當左邊界在startPos左邊，且符合`2l+r <= k`的情形時，那就是合法答案
```py
if axis[l] <= startPos:
    res = max(res, presum[r+1]-presum[l])
```

但要注意的是，我們再看一下`k=5`這個例子
```
k = 5
    <>>> # 先往左一步，再往右
   <<>   # 先往左兩步，再往右
<<<<<
  <<<>   # 先往右一步，再往左
    <>>  # 先往右兩步，再往左
     >>>>>
```

除了折返的情形外，我們還要考慮不折返的情形

我們在這步驟最後左邊界會抵達startPos，
```py
while axis[l] <= startPos and (axis[r]-startPos) + 2 * (startPos-axis[l]) > k:
    l += 1
```

但只要右邊界還沒走完`k`步，都是我們可以抵達的範圍
因此在右邊界axis[r]還小於等於 startPos+k之前，也都是合法答案
```py
elif axis[r] <= startPos + k:
    res = max(res, presum[r+1]-presum[l])
```

# Complexity

- time complexity

$$O(n)$$