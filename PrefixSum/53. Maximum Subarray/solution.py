# 1-D DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0

        # dp[i]: max sum of subarray which num ends at nums[i]
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        
        return max(dp)

# Prefix Sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        maxSum = nums[0]
        minSumUntilCurrent = inf
        for i in range(1, n+1):
            minSumUntilCurrent = min(minSumUntilCurrent, presum[i-1])
            maxSum = max(maxSum, presum[i] - minSumUntilCurrent)
        return maxSum
