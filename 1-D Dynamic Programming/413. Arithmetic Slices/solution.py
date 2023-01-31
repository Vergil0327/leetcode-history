# 2-D DP but we don't need to
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0

        dp = [[0]*(max(nums)-min(nums)+1) for _ in range(n)]

        for i in range(2, n):
            diff = nums[i-1] - nums[i-2]
            if nums[i] - nums[i-1] == diff:
                dp[i][diff] = dp[i-1][diff]+1
        return sum(map(sum, dp))

# 1-D DP
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0

        dp = [0] * n

        for i in range(2, n):
            diff = nums[i-1] - nums[i-2]
            if nums[i] - nums[i-1] == diff:
                dp[i] = dp[i-1]+1
        return sum(dp)