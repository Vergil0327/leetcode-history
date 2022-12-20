class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prices = [0,0] + prices # add [0,0] for shilfing index. avoid key error
        hold = [-inf] * (n+2) # max money after holding stock
        sold = [0] * (n+2) # max money after selling stock

        for i in range(2, n+2):
            hold[i] = max(hold[i-1], sold[i-2]-prices[i]) # i-2 for cooldown.
            sold[i] = max(sold[i-1], hold[i-1]+prices[i])
        return sold[-1] # max money should be accumulated until last day
        # return max(sold)