from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        leftSum, rightSum = nums[l], nums[r]

        operations = 0
        while l < r:
            if leftSum > rightSum:
                r -= 1
                rightSum += nums[r]
                operations += 1
            elif rightSum > leftSum:
                l += 1
                leftSum += nums[l]
                operations += 1
            else:
                l, r = l+1, r-1
                leftSum, rightSum = nums[l], nums[r]
        return operations
