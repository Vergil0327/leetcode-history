class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        m = len(s)
        
        low, high = "1", s
        while len(low) < len(high):
            low = "0" + low

        @cache
        def dfs(i, leading, lowerThanHigh, higherThanLow, changed):
            if i >= m:
                return 1 if changed else 0

            start = 0 if higherThanLow else int(low[i])
            end = 10 if lowerThanHigh else int(high[i])+1

            res = 0
            for d in range(start, end):
                if d in {3,4,7}: continue # invalid digits
                res += dfs(i+1,
                           leading and d == 0,
                           lowerThanHigh or d < int(high[i]),
                           higherThanLow or d > int(low[i]),
                           changed or d in {2,5,6,9})
            return res
        return dfs(0, True, False, False, False)
