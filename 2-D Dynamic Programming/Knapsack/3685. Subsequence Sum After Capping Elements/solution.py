class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)

        res = [False] * n

        nums.sort()

        dp = [False] * (k+1)
        dp[0] = True

        i = 0
        for x in range(1, n+1):
            while i < n and nums[i] < x:
                for _sum in range(k, 0, -1):
                    # dp[i][sum] = dp[i-1][sum - nums[i]]
                    if _sum - nums[i] < 0: break
                    dp[_sum] = dp[_sum] or dp[_sum - nums[i]]
                i += 1
            
            # 此時, dp[k]代表對於當前x來說, k是否是個合法subsequence sum
            res[x-1] = dp[k] # x: 1-indexed

            for cnt in range(n-i+1):
                extra = x * cnt
                if k - extra >= 0 and dp[k - extra]:
                    res[x-1] = True # x: 1-indexed
                    break
        return res