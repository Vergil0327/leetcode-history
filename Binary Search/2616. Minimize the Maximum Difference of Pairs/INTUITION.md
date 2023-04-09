# Intuition

這題是要求minimum maximum difference
對於任何要求minimum maximum的，都可以嘗試用binary search來做

由於我們並不關心index, 所以我們可以先排序
binary search核心框架如下:

```py
nums.sort()

l, r = 0, nums[-1] - nums[0]
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

最關鍵的就是如何check `mid`是不是可行解

當時比賽沒有想到，但其實如果只要要確認可不可行的話，我們可以Greedily check

框架肯定是像這樣，我們檢查對於當前的`mid`來說是不是能找到足夠的pairs來滿足 `pairs >= p`
```py
def check(mid):
    pairs = 0
    # logic here
    return pairs >= p
```

在排序過後的nums[i]來說, 他的最小difference肯定是周遭的兩個元素 nums[i-1]跟nums[i+1]
所以我們從i=0開始遍歷，只要`abs(nums[i]-nums[i+1])`符合條件，我們就取，然後i變為i+2
如果`abs(nums[i]-nums[i+1])`不符合條件, 那我們就將`i = i+1`, 看下一個相鄰的元素
最後就我們能不能在`mid`這difference下取到至少p個pairs

```py
def check(mid):
    pairs = 0
    i = 0
    while i < n:
        if i+1 < n and nums[i+1]-nums[i] <= mid:
            i = i+2
            pairs += 1
        else:
            i += 1
    return pairs >= p
```

ex. nums = 1 1 1 2 3 5 6

如果現在mid = 1
{1,1}, {1,2}, {3,5}-> 不合 -> {5,6}
