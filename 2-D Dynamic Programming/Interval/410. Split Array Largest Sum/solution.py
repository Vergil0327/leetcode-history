class Solution:
    def splitArray(self, nums: List[int], K: int) -> int:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        dp = [[inf] * (K+1) for _ in range(n+1)]
        nums = [0] + nums # to 1-indexed
        dp[0][0] = 0

        for i in range(1, n+1):
            for k in range(1, min(i, K)+1):
                # total = 0
                for j in range(i, k-1, -1):
                    # total += nums[j]
                    # dp[i][k] = min(dp[i][k], max(dp[j-1][k-1], total))
                    if presum[i]-presum[j-1] > dp[i][k] or dp[j-1][k-1] > dp[i][k]: break
                    dp[i][k] = min(dp[i][k], max(dp[j-1][k-1], presum[i]-presum[j-1]))
        return dp[n][k]
