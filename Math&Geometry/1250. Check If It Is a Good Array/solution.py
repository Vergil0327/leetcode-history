class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        GCD = nums[0]
        for num in nums:
            GCD = gcd(GCD, num)
            if GCD == 1: return True
        return GCD == 1