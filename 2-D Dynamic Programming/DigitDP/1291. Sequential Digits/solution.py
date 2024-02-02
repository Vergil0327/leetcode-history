class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low = str(low)
        high = str(high)
        while len(low) < len(high):
            low = "0" + low
        n = len(low)

        self.arr = []
        @cache
        def dfs(i, greaterThanLow, lowerThanHigh, digits):
            if i == n:
                self.arr.append(digits)
                return

            start = 0 if greaterThanLow else int(low[i])
            end = 10 if lowerThanHigh else int(high[i])+1

            for d in range(start, end):
                if digits == 0 or digits%10+1 == d:
                    dfs(i+1,
                        greaterThanLow or d > int(low[i]),
                        lowerThanHigh or d < int(high[i]),
                        digits*10+d)
        dfs(0, False, False, 0)
        return sorted(self.arr)
