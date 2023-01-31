class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        arr = sorted([[age, sc] for age, sc in zip(ages, scores)])
        dp = [0] * n # LIS, 
        for i in range(n):
            baseAge, score = arr[i][0], arr[i][1]
            dp[i] = score
            for j in range(i):
                if arr[j][0] < baseAge and arr[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)
                elif arr[j][0] == baseAge:
                    dp[i] = max(dp[i], dp[j] + score)
        return max(dp)
