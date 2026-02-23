class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp = nums.copy()

        for i in range(n):
            if i-1 >= 0:
                # skip i-th house
                dp[i] = max(dp[i], dp[i-1])
            
                # can rob
                if colors[i] != colors[i-1]:
                    dp[i] = max(dp[i], dp[i-1] + nums[i])

            if i-2 >= 0:
                # can rob
                dp[i] = max(dp[i], dp[i-2] + nums[i])            
        return dp[n-1]