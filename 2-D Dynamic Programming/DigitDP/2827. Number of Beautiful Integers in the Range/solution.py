class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        lo = str(low)
        hi = str(high)
        while len(lo) < len(hi):
            lo = "0"+lo
        
        n = len(hi)
        
        @cache
        def dfs(i, isGreaterThanLow, isLowerThanHigh, leadingZeros, oddCnt, evenCnt, remainder):
            if i == n:
                return 1 if remainder == 0 and evenCnt == oddCnt else 0
            
            start = 0 if isGreaterThanLow else int(lo[i])
            end = 10 if isLowerThanHigh else int(hi[i])+1
            
            res = 0
            for d in range(start, end):
                res += dfs(i+1,
                           isGreaterThanLow or d > int(lo[i]),
                           isLowerThanHigh or d < int(hi[i]),
                           leadingZeros and d == 0,
                           oddCnt + (1 if d >= 1 and d%2 != 0 else 0),
                           evenCnt + (1 if (not leadingZeros and d == 0 or d>=2 and d%2 == 0) else 0),
                           (remainder*10 + d)%k)
            return res
        
        return dfs(0, False, False, True, 0, 0, 0)
