# Intuition

這題首先必須想到的是:

對於subsequence來說，由於每個nums[i]都是可選可不選
所以即使我們對nums排序後，答案結果依然不變

因此我們可以試著對nums先排個序，這樣在找`min`跟`max`也方便很多

那在排序之後我們可發現`nums`會是這樣的一個情況
當前的nums[i]最為最小值, 最多能取到哪?

這時我們可以用binary search: `j = bisect.bisect_right(nums, target-nums[i])`
找出我們的上界**MAX**在哪

這時這段區間的總個數為`j-i`, 在nums[i]必選的情況下
由於`[i+1:j)`左閉右開這段區間的數可選可不選, 共有`2 ** (j-i-1)`種選擇的方式

```
nums = [MIN X X X X X X X X X] X
        i                      j
                            MX
```

這時計算的想法就很清楚了
我們由小到大遍歷i, 只要nums[i]+nums[i] <= target, 代表nums[i]是合法的
這時我們在找他的上界**MAX**在哪
再來就能計算出有多少種`MIN=nums[i]`的subsequence, i.e. `res += 2**(j-i-1)`
把全部可能加起來即可

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$

# Other Solution

[Two Pointers](../../Two%20Pointers/1498.%20Number%20of%20Subsequences%20That%20Satisfy%20the%20Given%20Sum%20Condition/)
