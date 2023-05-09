class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        dp = [[0]*n for _ in range(m)]

        for c in range(n):
            dp[0][c] = points[0][c]

        for r in range(1, m):
            rollingMax = -inf
            for c in range(n):
                rollingMax = max(rollingMax, dp[r-1][c]+c)
                dp[r][c] = max(dp[r][c], rollingMax - c + points[r][c])

            rollingMax = -inf
            for c in range(n-1, -1, -1):
                rollingMax = max(rollingMax, dp[r-1][c]-c)
                dp[r][c] = max(dp[r][c], rollingMax + c  + points[r][c])

        return max(dp[m-1])