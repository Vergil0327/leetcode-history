class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + stones[i-1]

        dp = [0] * (n+1)
        dp[1] = 0
        dp[2] = presum[n]

        for i in range(3, n+1):
            dp[i] = max(dp[i-1], presum[n-i+2]-dp[i-1])
        return dp[n]