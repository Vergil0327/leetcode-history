class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        high = str(n)
        low = "1"
        while len(low) < len(high):
            low = "0" + low

        length = len(high)

        @cache
        def dfs(i, hasLeadingZero, isGreaterThanLowerbound, isLowerThanUpperbound, state):
            if i == length: return 1
            start = 0 if isGreaterThanLowerbound else int(low[i])
            end = 10 if isLowerThanUpperbound else int(high[i])+1

            res = 0
            for d in range(start, end):
                # digit `d` is already used
                if d > 0 and (state>>d)&1: continue
                if not hasLeadingZero and d == 0 and (state>>d)&1: continue
                
                nxt = state
                if d > 0 or not hasLeadingZero:
                    nxt |= (1<<d)

                res += dfs(i+1,
                    hasLeadingZero and d == 0,
                    isGreaterThanLowerbound or d > int(low[i]),
                    isLowerThanUpperbound or d < int(high[i]),
                    nxt)
            return res
        return dfs(0, True, False, False, 0)
