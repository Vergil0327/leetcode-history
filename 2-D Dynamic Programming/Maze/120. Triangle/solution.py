# 2-D DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[inf]*(n+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1, n+1):
            for j in range(i):
                dp[i][j] = dp[i-1][j]+triangle[i-1][j]
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+triangle[i-1][j])

        return min(dp[n])

# Space-Optimized
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        prevdp = [inf]*(n+1) # store dp[i-1][0...j] state
        dp = [inf]*(n+1)     # store dp[i][0...j] state
        prevdp[0] = 0

        for i in range(1, n+1):
            for j in range(i):
                dp[j] = prevdp[j]+triangle[i-1][j]
                if j-1 >= 0:
                    dp[j] = min(dp[j], prevdp[j-1]+triangle[i-1][j])
            prevdp, dp = dp, prevdp

        return min(prevdp)