class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        nums = [0] + nums
        dp = [[0]*k for _ in range(n+1)]
        for i in range(1, n+1):
            # only nums[i] itself
            dp[i][nums[i]%k] += 1

            for r in range(k):
                x = (r*nums[i])%k
                dp[i][x] += dp[i-1][r]
        
        res = [0] * k
        for i in range(1, n+1):
            for r in range(k):
                res[r] += dp[i][r]
        return res