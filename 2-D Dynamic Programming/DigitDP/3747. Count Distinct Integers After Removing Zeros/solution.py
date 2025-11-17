class Solution:
    def countDistinct(self, n: int) -> int:
        low, high = "1", str(n)
        while len(low) < len(high):
            low = "0" + low

        m = len(high)
        @cache
        def dfs(i, lowerThanHigh, greaterThanLow, leadingZero):
            if i >= m: return 1 if not leadingZero else 0
            start = 0 if greaterThanLow else int(low[i])
            end = 10 if lowerThanHigh else int(high[i])+1

            res = 0
            for d in range(start, end):
                if d == 0:
                    # only allow `0` in leading zeros
                    if leadingZero:
                        res += dfs(i+1, lowerThanHigh or d < int(high[i]), greaterThanLow or d > int(low[i]), True)
                else:
                    res += dfs(i+1, lowerThanHigh or d < int(high[i]), greaterThanLow or d > int(low[i]), False)
            return res
        
        return dfs(0, False, False, True)