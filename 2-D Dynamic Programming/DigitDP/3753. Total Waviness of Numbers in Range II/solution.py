class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        low = str(num1)
        high = str(num2)
        while len(low) < len(high):
            low = "0" + low

        @cache
        def dfs(i, valid, isGreaterThanLowerbound, isLowerThanUpperbound, prev, mid, count):
            if i == len(high): return count

            start = 0 if isGreaterThanLowerbound else int(low[i])
            end = 10 if isLowerThanUpperbound else int(high[i]) + 1
            valid = valid or prev > 0
            res = 0
            for d in range(start, end):

                x = int(
                    prev != -1
                    and valid
                    and ((prev < mid > d) or (prev > mid < d))
                )

                res += (
                    dfs(
                        i + 1,
                        valid,
                        isGreaterThanLowerbound or d > int(low[i]),
                        isLowerThanUpperbound or d < int(high[i]),
                        mid,
                        d,
                        count + x,
                    )
                )
            return res

        return dfs(0, False, False, False, -1, -1, 0)

