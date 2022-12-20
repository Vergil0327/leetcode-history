class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold = [-inf] * (n+1)
        sold = [0] * (n+1)
        prices = [0] + prices # shift index to make index be consistent with hold[i] & sold[i]
        
        for i in range(1, n+1):
            hold[i] = max(hold[i-1], sold[i-1]-prices[i])
            sold[i] = max(sold[i-1], hold[i-1]+prices[i]-fee)
        return sold[-1]
        # return max(sold)