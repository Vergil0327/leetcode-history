class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]

        for h, w, p in prices:
            dp[h][w] = p

        for i in range(1, m+1):
            for j in range(1, n+1):
                for cut in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[i-cut][j] + dp[cut][j])

                for cut in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][j-cut] + dp[i][cut])

        return dp[m][n]
