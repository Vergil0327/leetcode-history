class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        res = 0
        l = r = 0
        while r < n:
            num = nums[r]
            r += 1

            while l < r and num != 0:
                l += 1
            res += r-l
            
        return res

# Optimized
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                res += zeros
            else:
                zeros = 0
        return res