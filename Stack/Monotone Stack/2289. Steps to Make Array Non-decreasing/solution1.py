class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        dp = [0] * n
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                dp[i] = max(dp[i]+1, dp[stack.pop()])
            stack.append(i)
        return max(dp)
