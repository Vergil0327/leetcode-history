class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        prevIdx = res = 0
        for i in range(1, n):
            if nums[i] > nums[prevIdx]:
                res += nums[prevIdx] * (i-prevIdx)
                prevIdx = i

        if prevIdx != n-1:
            res += nums[prevIdx] * (n-1-prevIdx)

        return res
    
# Concise
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        mx = res = 0
        for i in range(n - 1):
            mx = max(mx, nums[i])
            res += mx
        return res
