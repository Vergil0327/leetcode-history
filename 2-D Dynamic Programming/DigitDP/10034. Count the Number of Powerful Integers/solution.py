class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low, high = str(start), str(finish)
        while len(low) < len(high):
            low = "0" + low
            
        n, m = len(low), len(s)

        @cache
        def dfs(i, leading, lowerThanHigh, higherThanLow):
            if i == n: return 1

            start = 0 if higherThanLow else int(low[i])
            end = 10 if lowerThanHigh else int(high[i])+1
            end = min(end, limit+1)
            res = 0
            for d in range(start, end):
                if i >= n-m and str(d) != s[i-(n-m)]: continue
                    
                res += dfs(i+1,
                           leading and d == 0,
                           lowerThanHigh or d < int(high[i]),
                           higherThanLow or d > int(low[i]))
            return res
        return dfs(0, True, False, False)