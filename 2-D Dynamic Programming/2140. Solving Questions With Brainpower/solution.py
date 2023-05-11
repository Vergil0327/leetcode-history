class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        dp[n-1] = questions[n-1][0]
        for i in range(n-2, -1, -1):
            score, k = questions[i]
            dp[i] = max(dp[i+1], (dp[i+k+1] if i+k+1 < n else 0)+score)

        return dp[0]