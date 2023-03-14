class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = 0
        n = len(nums)
        curr = 1
        res = 0
        while r < n:
            curr *= nums[r]
            r += 1

            while l < r and curr >= k:
                curr //= nums[l]
                l += 1
            if curr < k:
                res += r-l
        return res
