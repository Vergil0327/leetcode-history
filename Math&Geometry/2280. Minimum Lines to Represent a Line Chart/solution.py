class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n < 2: return 0

        stockPrices.sort()

        res = 1
        for i in range(1, n-1):
            x1, y1 = stockPrices[i-1]
            x2, y2 = stockPrices[i]
            x3, y3 = stockPrices[i+1]
            # m1 = (y2-y1) / (x2-x1)
            # m2 = (y3-y2) / (x3-x2)
            # m1 == m2 => (y2-y1) / (x2-x1) == (y3-y2) / (x3-x2)
            # => (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1)
            if (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1): continue
            res += 1
        return res