class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones == 0 or ones == len(nums): return 0
        
        nums = nums + nums

        n = len(nums)
        l = r = window_sum = 0
        res = n//4
        while r < n:
            window_sum += nums[r]
            r += 1

            while l < r and r-l >= ones:
                res = min(res, r-l-window_sum)
                window_sum -= nums[l]
                l += 1
            
        return res

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        if ones == 0 or ones == len(nums): return 0

        n = len(nums)
        l = r = window_sum = 0
        res = n//2
        while r < n*2:
            window_sum += nums[r%n]
            r += 1

            while l < r and r-l >= ones:
                res = min(res, r-l-window_sum)
                window_sum -= nums[l%n]
                l += 1
            
        return res