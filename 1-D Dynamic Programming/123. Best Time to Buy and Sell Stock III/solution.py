# 4 state transfer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, sold1, hold2, sold2 = -inf, 0, -inf, 0
        for i in range(len(prices)):
            hold1Prev, sold1Prev, hold2Prev, sold2Prev = hold1, sold1, hold2, sold2
            hold1 = max(hold1Prev, 0-prices[i])
            sold1 = max(sold1Prev, hold1Prev+prices[i])
            hold2 = max(hold2Prev, sold1Prev-prices[i])
            sold2 = max(sold2Prev, hold2Prev+prices[i])
        return max(sold1, sold2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxTx = 2
        dp = [[[0]*2 for k in range(maxTx+1)] for _ in range(len(prices)+1)]

        for k in range(1, maxTx+1):
            dp[0][k][1] = float("-inf")

        for i, price in enumerate(prices, start=1):
            for k in range(maxTx, 0, -1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+price)
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-price)

        return dp[-1][maxTx][0]