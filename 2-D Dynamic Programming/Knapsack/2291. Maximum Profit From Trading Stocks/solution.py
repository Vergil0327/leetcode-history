from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        present = [0] + present
        future = [0] + future
        profit = [future[i]-present[i] for i in range(n+1)]

        dp = [[-float("inf")] * (budget+1) for _ in range(n+1)]

        for j in range(budget+1):
            dp[0][j] = 0

        for i in range(1, n+1):
            for j in range(budget+1):
                dp[i][j] = dp[i-1][j]
                if j-present[i] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-present[i]] + profit[i])
        return dp[n][budget]



# profit = X X X X X X X
#                      i
        