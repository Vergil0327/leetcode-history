# O(n) Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curr = 0
        res = inf
        while r < len(nums):
            curr += nums[r]
            r += 1

            while curr >= target:
                res = min(res, r-l)
                curr -= nums[l]
                l += 1
        return res if res != inf else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = [0] + list(accumulate(nums))
        
        res = inf
        for i in range(1, len(nums)+1):
            prefixSum = presum[i-1] + target
            j = bisect.bisect_left(presum, prefixSum)
            if j < len(presum):
                res = min(res, j-i+1)
        return res if res != inf else 0