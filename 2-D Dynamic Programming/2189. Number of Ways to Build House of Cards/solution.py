class Solution:
    def houseOfCards(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n//2+1)]

        # base case
        # because i strats from 1,
        # we need to consider value of dp[0][j]
        dp[0][0] = 1

        for i in range(1, n//2+1):
            used = 2 + 3*(i-1)
            for j in range(n+1):
                dp[i][j] = dp[i-1][j] + (dp[i-1][j-used] if j-used >= 0 else 0)
        return dp[n//2][n]
