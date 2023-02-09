# Intuition

可以看出 x 的存在範圍就在`[0, len(nums)]`
我們就逐個試即可，要找出 `>= x` 的位置那就是透過bisect.bisect_left找出lowerbound
然後判斷 (n-i) 有沒有等於 x 即可
如果沒有任何的x能被找出來，那就返回`-1`

time: $O(nlogn)$

# Most Optimized Solution

[HuifengGuan - bucket sort + suffix sum](https://www.youtube.com/watch?v=EyB0iYwKF84)

```py
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        bucket = [0] * (n+1)
        for num in nums:
            # if num >= n:
            #     bucket[n] += 1
            # else:
            #     bucket[num] += 1
            bucket[min(n, num)] += 1
        
        count = 0
        for x in range(n, 0, -1):
            count += bucket[x]
            if x == count: return x
        return -1

```
