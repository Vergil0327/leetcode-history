class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix_prices = list(accumulate(prices, initial=0))
        presum = [0]
        for p, st in zip(prices, strategy):
            presum.append(presum[-1] + p*st)

        j = 0
        res = presum[n]
        for i in range(n-k+1):
            while j < n and j - i < k:
                j += 1

            # Set the first k / 2 elements to 0 (hold).
            # Set the last k / 2 elements to 1 (sell).
            # only earned second-half
            mid = prefix_prices[j]-prefix_prices[j-k//2]
            res = max(res, presum[i] + mid + presum[n]-presum[j])
        return res
