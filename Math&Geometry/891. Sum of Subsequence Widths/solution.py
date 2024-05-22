class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        res = 0
        for i in range(n):
            contribMin = nums[i] * pow(2, n-i-1, mod)
            contribMax = nums[i] * pow(2, i, mod)
            res = (res + contribMax-contribMin) % mod
        return res
