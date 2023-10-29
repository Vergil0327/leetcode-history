class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf]*n

        # base case
        dp[0] = max(0, k-nums[0])
        dp[1] = max(0, k-nums[1])
        dp[2] = max(0, k-nums[2])
        for i in range(3, n):
            dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + max(0, k-nums[i])
        return min(dp[-1], dp[-2], dp[-3])
