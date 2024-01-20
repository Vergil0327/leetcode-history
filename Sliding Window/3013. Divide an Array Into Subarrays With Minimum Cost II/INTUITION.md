# Intuition

塞k-1個隔板隔出k個subarray, 第一個隔板距離跟最後一個隔板距離相差不可超過dist
也就是撇除掉i=0的第一個cost, 第二個cost跟最後一個cost 兩者代表cost的num的位置(index)相差不可超過dist
代表我們需要一個長度為dist+1的sliding window, 然後從這個sliding window中取出前k-1個最小的數作為cost
持續找出全局最小解

TLE version:
```py
from sortedcontainers import SortedList
res = inf
l = r = 1
n = len(nums)
sl = SortedList()
while r < n:
    sl.add(nums[r])
    r += 1
    
    while l < r and r-l > dist+1:
        sl.remove(nums[l])
        l += 1
    if len(sl) >= k-1:
        res = min(res, nums[0] + sum(sl[:k-1]))
return res
```

sum(sl[:k-1])這步太耗時間了, 所以我們得想個辦法改進計算前k-1 sum的方法

我們將原本的一個sorted list拆分成兩部分, 分別是sl1, sl2, 個別都還是SortedList
sl1: 維護sliding window內前k-1小的數
sl2: 維護剩餘的其他數

只要一想到這個, 後面就會豁然開朗了
一樣用雙指針`l`, `r`維護一個長度為dist+1的sliding window, 並持續移動雙指針即可:

這邊為了後面方便, 因為i=0這個數必定得取作cost, 能操作只有後面k-1個cost, 所以我們先直接`k-=1`, 然後找minimum ksum

```py
n = len(nums)
k -= 1

sl = SortedList(nums[1:dist+2])
sl1, sl2 = SortedList(sl[:k]), SortedList(sl[k:])
res = ksum = sum(sl1)
# 雙指針
for l in range(1, n - dist - 1):
    r = l+dist+1

    # todo
```

左指針`l`移動代表要移除, 我們就看要移除的是在sl1還sl2, 只有sl1的部分會牽扯到cost, 所以:
```py
if nums[l] in sl1:
    ksum -= nums[l]
    sl1.remove(nums[l])
else:
    sl2.remove(nums[l])
```

再來移動右指針`r`, 並看nums[r]要加入sl1, 還sl2, 一樣只有加入到sl1時才會需要更新ksum

```py
if len(sl1) == 0 or sl1[-1] >= nums[r]:
    sl1.add(nums[r])
    ksum += nums[r]
else:
    sl2.add(nums[r])
```

加入後記得調整sl1, sl2長度, 將sl1維持k個:

```py
while len(sl1) > k:
    ksum -= sl1[-1]
    sl2.add(sl1.pop())
while len(sl1) < k:
    ksum += sl2[0]
    sl1.add(sl2.pop(0))
```

總時間複雜度就是nlog(n)