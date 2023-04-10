class Solution:
    def largestSumOfAverages(self, nums: List[int], K: int) -> float:
        n = len(nums)

        nums = [0] + nums # to 1-indexed
        dp = [[-inf] * (K+1) for _ in range(n+1)]

        dp[0][0] = 0

        for i in range(1, n+1):
            for k in range(1, min(i, K)+1):
                total = 0
                for j in range(i, k-1, -1):
                    total += nums[j]
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + total/(i-j+1))
        return dp[n][K]
                