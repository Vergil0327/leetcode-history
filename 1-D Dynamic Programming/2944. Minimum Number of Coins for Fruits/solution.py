class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n =len(prices)
        prices = [0]+prices # to 1-indexed

        @cache
        def dfs(i, freeMostFarAt):
            if i > n or freeMostFarAt > n: return 0

            res = inf
            if i <= freeMostFarAt:
                res = min(dfs(i+1, freeMostFarAt), dfs(i+1, max(freeMostFarAt, i+i)) + prices[i])
            else:
                res = dfs(i+1, max(freeMostFarAt, i+i)) + prices[i]
            return res

        return dfs(1, 0) # 1-indexed
        