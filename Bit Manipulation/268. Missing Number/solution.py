# Intuition:
# num^num = 0
# 0^num = num^0 = num
# XOR from 1 to n one time
# then XOR with nums
# the result should be answer
# time: O(n)
# space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for num in nums:
            res ^= num
        return res