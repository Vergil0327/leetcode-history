class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        low, high = str(l), str(r)
        while len(low) < len(high):
            low = "0" + low

        n = len(high)

        @cache
        def dfs(i, leadingZero, isGreaterThanLow, isLowerThanHigh, prod, total):
            if i >= n: return int(prod%total == 0)

            start = 0 if isGreaterThanLow else int(low[i])
            end = 10 if isLowerThanHigh else int(high[i])+1

            res = 0
            for d in range(start, end):
                p = prod * d if d > 0 or not leadingZero else prod
                res += dfs(i+1,
                           leadingZero and d == 0,
                           isGreaterThanLow or d > int(low[i]),
                           isLowerThanHigh or d < int(high[i]),
                           p,
                           total+d)
            return res
        return dfs(0, True, False, False, 1, 0)