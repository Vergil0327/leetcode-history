# Greedy
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0

        length = 1 # base case, nums[0] always be a valid wiggle point
        prevSlope = inf
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] > 0:
                slope = 1
            elif nums[i]-nums[i-1] < 0:
                slope = -1
            else:
                slope = prevSlope

            if slope != prevSlope:
                length += 1
            prevSlope = slope
        
        return length

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[0] = longest wiggle seq. which ends with positive slope
        # dp[1] = longest wiggle seq. which ends with negative slope
        dp = [1, 1]
        for i in range(1, n):
            if nums[i]-nums[i-1] > 0: # positive to negative wiggle
                dp[1] = dp[0] + 1 
            if nums[i]-nums[i-1] < 0: # negative to positive wiggle
                dp[0] = dp[1] + 1
        return max(dp)