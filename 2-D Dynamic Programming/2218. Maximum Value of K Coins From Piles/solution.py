class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        n = len(piles)
        presum = []
        for i in range(n):
            m = len(piles[i])

            presum.append([0] * (m+1))
            for j in range(1, m+1):
                presum[i][j] = presum[i][j-1] + piles[i][j-1]
        
        dp = [[-inf] * (K+1) for _ in range(n)]
        for i in range(n):
            m = len(piles[i])
            for j in range(K+1):
                for k in range(min(j, m)+1):
                    dp[i][j] = max(dp[i][j], (dp[i-1][j-k] if i-1>=0 else 0) + presum[i][k])
        return dp[n-1][K]

# dp[i][j]: the maximum total value considering first i piles and choosing j coins

# [X X X] X X X X X X
# [X X X X X X] X X X
# [X X X X] X X X X X