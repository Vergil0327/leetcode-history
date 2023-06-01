from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def check(ops, x, y):
            extra = (x-y)*ops
            for num in nums:
                curr = num-y*ops
                if curr > 0:
                    extra -= curr
                    if extra < 0: return False
            return True

        l, r = 0, max(nums)
        while l < r:
            mid = l + (r-l)//2
            if check(mid, x, y):
                r = mid
            else:
                l = mid+1
        return l