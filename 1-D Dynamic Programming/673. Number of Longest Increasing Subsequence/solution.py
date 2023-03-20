class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        
        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        
        res = 0
        mx = max(dp)
        for i in range(n):
            if dp[i] == mx:
                res += cnt[i]
        return res