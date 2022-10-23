# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/852280/Python-DP-Solution
# https://labuladong.github.io/algo/1/13/
class DPSolution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # dp[i][0 or 1]
        dp = [[0] * 2 for _ in range(N+1) ]
        
        # dp[i][0] not hold
        # dp[i][1] hold stock
        dp[0][1] = float("-inf")
        for i, p in enumerate(prices, 1): 
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + p) # hold or sold -> hold
            dp[i][1] = max(dp[i-1][1], -p) # hold or buy -> hold, choose one single day to buy: -prices[i]

        return dp[N][0]