from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(x):
            return a * (x**2) + b*x + c
        
        n = len(nums)
        l, r = 0, n-1
        res = [0]*n
        if a > 0:
            for i in range(n-1, -1, -1):
                left, right = f(nums[l]), f(nums[r])
                if right > left:
                    res[i] = right
                    r -= 1
                else:
                    res[i] = left
                    l += 1
            return res
        elif a < 0:
            for i in range(n):
                left, right = f(nums[l]), f(nums[r])
                if right < left:
                    res[i] = right
                    r -= 1
                else:
                    res[i] = left
                    l += 1
            return res
        else: # a == 0
            for i in range(n):
                res[i] = f(nums[l])
                l += 1
                
            return res if b >= 0 else list(reversed(res))
            