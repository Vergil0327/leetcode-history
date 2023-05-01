# Binary Search 


## Intuition

這題要找的是讓這整段區間在數值上是連續的最小操作數是多少

首先因為index並不影響, 所以我們可以先對nums排序
排序後對於每個nums[i]來說, 以`nums[i]`作為左端點的區間, 其右端點為`nums[i]+n-1`

也就是說我們如果遍歷左端點, 右端點也會相對應的確定
我們這時就看`[nums[i], nums[i]+n-1]`這段區間已經有多少數值連續的元素

如果說`target = nums[i]+n-1`
那我們可以用binary search找出這段區間的右端點在哪
那這樣我們需要的操作數就是將`nums[i]`之前的元素以及從`nums[j]`開始之後的每個元素
把他們全加進`nums[i:j)`區間的次數, 也就是這些元素的個數
所以是全部的個數`n`減去已經是連續區間的個數`j-i`, 亦即`n-(j-i)`
所以我們僅需要遍歷每個nums[i]找出以其為左端點所需要的操作數即可

```
j = bisect_right(arr, target)
X X X X X [X X X X X X X X X X] X X X X X
           i                    j
```

但有個前提是, `nums[i:j)`這區間內的每個數必須是**unique**的
所以我們先將nums去除重複的數並排序
`arr = sorted(set(nums))`
這樣一來我們便能在`arr`上遍歷每個arr[i]作為左端點
並用binary search找出右端點
然後看裡頭已經有多少unique且連續的數存在, 將len(nums)減去這段區間的個數後
就是我們需要的操作數

```py
res = inf
for i, num in enumerate(arr):
    target = num+(n-1)
    j = bisect.bisect_right(arr, target)
    res = min(res, n-(j-i))
```

## Other Solution

[Sliding Window](../../Sliding%20Window/2009.%20Minimum%20Number%20of%20Operations%20to%20Make%20Array%20Continuous/)