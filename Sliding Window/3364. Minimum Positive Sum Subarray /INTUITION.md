# Intuition

這題數據規模很小, 其實用O(n^2)就能過了, 但有沒有更好的解法?

## Optimization

對於一段區間和, 我們可以利用prefix sum來快速得到
首先先求得prefix sum:

```py
presum = list(accumulate(nums, initial=0))
```

> 這邊我們prefix sum為**1-indexed**

那有了prefix sum後, 我們當前想要的合法區間和為:

```
min(presum[i] - presum[k]) where l <= i-k <= r
```

該如何快速查找?

這時就要利用到有序容器: **SortedList**

核心思想是:
我們目標是將`presum[k]`加入到有序容器**SortedList**裡, 並且`k`符合`l <= i-k <= r`
那這樣我們就能透過binary search找出最接近presum[i]但小於presum[i]的區間和
也就是**大於等於presum[i]**的前一個位置
那這樣`presum[i]-presum[k]`就會是當前符合長度考量的最小區間和


因此, 首先我們遍歷prefix sum, 範圍[1,n]

1. 過程中一但長度`i`**大於等於**`l`, 這時就已經是合法長度(l <= i <= r)了
我們將前段區間和, prefix sum[i-l]加入到有序容器`SortedList`裡

2. 再來一但`i`**大於**`r`, 我們就必須將有序容器裡的prefix sum[i-r-1]給移除掉, 因為這時prefix sum[i-r-1]已經不是合法的`presum[k]`了. (size: i-(i-r-1)=r+1 > r)

在做完以上操作後, 我們的有序容器**SortedList**裡面存放的就是合法的`presum[k]`, 這時:

`presum[i]-presum[k] for presum[k] in SortedList`

所以當前合法的最小區間和為:

```py
k = sl.bisect_left(presum[i])-1
if k >= 0:
    res = min(res, presum[i]-sl[k])
```

time: O(nlogn)
space: O(n)