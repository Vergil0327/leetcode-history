class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        presum = list(accumulate(nums, initial=0))
        
        n = len(nums)
        res = r = 0
        for l in range(n):
            while r < n and presum[r+1]-presum[(l+r+1)//2] - (presum[(l+r)//2+1] - presum[l]) <= k:
                r += 1
            res = max(res, r-l)
            
        return res