class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = l = r = 0
        window = 0

        while r < n:
            num = nums[r]
            r += 1

            while l < r and window&num != 0:
                window ^= nums[l]
                l += 1
            window |= num

            res = max(res, r-l)
        return res