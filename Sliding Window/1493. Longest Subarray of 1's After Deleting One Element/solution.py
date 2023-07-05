class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        res = zero = 0
        l = r = 0
        while r < n:
            if nums[r] == 0:
                zero += 1
            r += 1

            while l < r and zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1
            res = max(res, r-l-1) # must remove 1 element
        return res