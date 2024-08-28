class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = j = 0
        for i in range(n):
            j = max(i+1, j)
            while j < n and prices[j] == prices[j-1]-1:
                j += 1
            res += j-i
        return res

