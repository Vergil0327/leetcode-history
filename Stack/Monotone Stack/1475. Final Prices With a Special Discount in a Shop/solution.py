class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        res = prices.copy()
        stack = []
        for j in range(n):
            while stack and prices[stack[-1]] >= prices[j]:
                i = stack.pop()
                res[i] -= prices[j]
            stack.append(j)
        return res
