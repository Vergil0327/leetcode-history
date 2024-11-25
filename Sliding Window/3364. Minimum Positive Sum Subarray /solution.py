class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = inf
        for j in range(len(nums)):
            tot = 0

            # j-i+1 <= r => i >= j-r+1
            for i in range(j, max(-1, j-r), -1):
                tot += nums[i]
                if l <= j-i+1 and tot > 0:
                    res = min(res, tot)
                
        return res if res < inf else -1
    

## Optimization: Sliding Window + Sorted List
from sortedcontainers import SortedList
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = inf

        presum = list(accumulate(nums, initial=0))
        sl = SortedList()

        # we want min(presum[i+1] - presum[k]) where l <= i+1-k <= r
        for i in range(1, len(nums)+1):
            if i >= l:
                sl.add(presum[i-l])

            if i > r:
                sl.remove(presum[i-r-1])
            
            k = sl.bisect_left(presum[i])-1
            if k >= 0:
                res = min(res, presum[i]-sl[k])
        return res if res < inf else -1
