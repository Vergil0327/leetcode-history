class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)

        # to 1-indexed, match with dp
        satisfaction = [0] + satisfaction

        # dp[i][j]: the maximum sum of like-time coefficient considering first i dishes and choose j dishes
        dp = [[-inf] * (n+1) for _ in range(n+1)]
        
        dp[0][0] = 0
        for i in range(1, n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + satisfaction[i] * j)

        return max(dp[n])