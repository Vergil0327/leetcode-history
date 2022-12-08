# Intuition
# 1. any num XOR itself = 0
# 2. 0 ^ num = num
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res