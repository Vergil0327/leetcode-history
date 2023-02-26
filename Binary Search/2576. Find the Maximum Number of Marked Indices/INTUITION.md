# Intuition

我們的目的是盡可能地找到(i, j) pair where 2 * nums[i] <= nums[j] and i != j

由於是找pair，最多就n//2的pair對，也就是最大操作數為n

由於i, j不論先後，我們僅考慮數值，所以我們可以先對nums排序
然後會發現當配對數的多寡的可行性具有單調性，因此我們可以用binary search by value去猜最大配對數
找到之後最大操作數就是`最大配對數 * 2`

核心框架為:

```py
l, r = 0, n//2
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l*2
```

至於檢查當前`mid`個配對能不能找出來的helper function `check`為:

我們可以將前`mid`大的數當作nums[j]，然後看剩下的nums[0]到nums[j-mid]作為nums[i]能不能找到至少`mid`個配對，如此一來即可知道當前猜的`mid`是不是可行解

```py
def check(targetNumPair):
    pairs = 0
    j = n-1
    for i in range(j-targetNumPair, -1, -1):
        if nums[i] * 2 <= nums[j]:
            j -= 1
            pairs += 1
    return pairs >= targetNumPair
```

# Optimized

首先我們知道最大配對數為`n//2`，所以其實最佳策略就是看後半nums[n//2:]最多能在前半nums[:n//2]找到多少個配對

找的方式其實就是我們前面的helper function `check`
我們在最nums排序後，挑出最大的`n//2`個數當作nums[j], 然後剩下的數作為nums[i]
那們最佳策略肯定是，最大的nums[j]跟最大並且符合條件的nums[i]配對在一起
如此一來，最多能配對的數目即是最佳解

```py
j = n-1
ops = 0
for i in range(n//2-1, -1, -1):
    if nums[i] * 2 <= nums[j]:
        j -= 1
        ops += 2
return ops
```