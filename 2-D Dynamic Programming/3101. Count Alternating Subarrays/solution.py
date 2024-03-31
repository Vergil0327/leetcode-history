class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            dp[i][nums[i]] = 1
            
        for i in range(1, n):
            dp[i][nums[i]] += dp[i-1][1-nums[i]]
        
        res = 0
        for i in range(n):
            res += sum(dp[i])
        return res
