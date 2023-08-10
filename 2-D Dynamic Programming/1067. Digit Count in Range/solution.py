class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        low = str(low)
        high = str(high)
        while len(low) < len(high):
            low = "0" + low

        n = len(high)
        def dfs(i, dCount, isGreaterThanLow, isLowerThanHigh, hasLeadingZero):
            if i == n: return dCount

            start = 0 if isGreaterThanLow else int(low[i])
            end = 10 if isLowerThanHigh else int(high[i])+1
            res = 0
            for digit in range(start, end):
                res += dfs(i+1,
                           dCount + (1 if digit == d else 0),
                           isGreaterThanLow or digit > int(low[i]),
                           isLowerThanHigh or digit < int(high[i]),
                           hasLeadingZero and digit == 0)
            return res
        return dfs(0, 0, False, False, True)

