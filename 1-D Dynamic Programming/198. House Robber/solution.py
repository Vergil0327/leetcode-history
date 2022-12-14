class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            tmp = max(nums[i] + rob1, rob2)
            rob1, rob2 = rob2, tmp
        return rob2