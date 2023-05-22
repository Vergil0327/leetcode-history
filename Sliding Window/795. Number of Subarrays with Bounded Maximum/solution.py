class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        
        def lessThan(k):
            res = l = r = 0
            mx = -inf
            while r < n:
                mx = max(mx, nums[r])
                r += 1

                while l < r and mx > k:
                    mx = -inf
                    l = r
                res += r-l
            return res

        return lessThan(right) - lessThan(left-1)
    
# One Pass
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)

        res = 0
        l = r = -1
        for i in range(n):
            if nums[i] > right:
                l = r = i
                continue
            if nums[i] >= left:
                r = i
            res += r-l
        return res