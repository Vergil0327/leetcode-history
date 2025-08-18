class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: abs(x))

        n = len(nums)
        
        r = res = 0
        for l in range(n):
            while r < n and abs(nums[r]) <= 2 * abs(nums[l]):
                r += 1
            res += r-l-1 # 對於左端點來說, 有r-l-1個右端點
        return res