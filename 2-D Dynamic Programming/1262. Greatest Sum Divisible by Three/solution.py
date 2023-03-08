class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i][mod]: maximum possible sum considering array[:i] where the current sum modulo 3 is equal to mod.
        dp = [[-inf]*3 for _ in range(n+1)]
        dp[0][0] = 0

        nums = [0] + nums
        for i in range(1, n+1):
            mod = nums[i]%3
            for j in range(3):
                dp[i][j] = max(dp[i-1][j], dp[i-1][(3+j-mod)%3] + nums[i])
        
        return dp[n][0]
