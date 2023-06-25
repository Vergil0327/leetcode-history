class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        n = len(nums)
        i = 0
        while i < n and nums[i] == 0:
            i += 1
        if i == n: return 0
        
        res = 1
        while i < n:
            j = i+1
            while j < n and nums[j] == 0:
                j += 1
            split = (j-(i+1))+1
            if j < n and nums[j] == 1:
                res *= split
            i = j
        return res%mod
        
# [0,1,0,0,1,0,0,1]