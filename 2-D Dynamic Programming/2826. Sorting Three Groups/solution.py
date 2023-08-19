class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums = nums
        dp = [[inf] * 4 for _ in range(n)]

        for j in range(1, 4):
            dp[0][j] = 0 if j == nums[0] else 1

        for i in range(1, n):
            for prevJ in range(1, 4):
                for j in range(prevJ, 4):
                    dp[i][j] = min(dp[i][j], dp[i-1][prevJ] + (1 if j != nums[i] else 0))

        return min(dp[n-1])
