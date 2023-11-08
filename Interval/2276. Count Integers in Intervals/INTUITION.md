# Intuition

一開始想到的是利用MAP來紀錄{left: right} interval

由於`1 <= left <= right <= 10^9`, 所以如果能維護一個有序的intervals那就可以用binary search來定位更新, 方便很多

所以想到的是利用**SortedDict**來紀錄每個interval {left: right}
並維護一個變數`cnt`紀錄當前的`sum(interval.length)`

那再來就看該如何更新或合併interval:

```
MAP: {left1: right1, left2: right2}
left1-----right1       left2-----------right2
        left---right
```

如果現在有個新interval: {left: right}
首先我們能用`j = bisect_right(right)`來找出第一個大於right的區間, 該區間為當前[left,right]區間的右側, 不受影響
真正受影響的為從`j-1`開始往回找的interval, 我們要把他們通通合併起來

判斷條件為: **intv.peekitem(j-1)[1] >= left**
只要上述條件滿足, 代表該區間與當前[left,right]區間有所重疊, 我們把它merge成新的區間, 並更新區間長度`self.cnt`: 

```py
while j-1 >= 0 and intv.peekitem(j-1)[1] >= left:
    left = min(left, intv.peekitem(j-1)[0])
    right = max(right, intv.peekitem(j-1)[1])
    self.cnt -= intv.peekitem(j-1)[1] - intv.peekitem(j-1)[0] + 1
    intv.popitem(j-1)
    j -= 1
```

等到跳出循環, 代表已無區間跟當前[left,right]重疊, 我們可以放心更新區間以及`self.cnt`：
```py
intv[left] = right
self.cnt += right-left+1
```