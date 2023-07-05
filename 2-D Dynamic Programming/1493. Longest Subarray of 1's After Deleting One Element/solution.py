class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0,0] for _ in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = -inf
        for i in range(1, n):
            if nums[i]:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            else:
                if nums[i-1] == 1:
                    dp[i][0] = 0
                    dp[i][1] = dp[i-1][0]
                else:
                    dp[i][0] = 0
                    dp[i][1] = 0

        res = -inf
        for i in range(n):
            res = max(res, dp[i][1])
        return res if res != -inf else n-1
