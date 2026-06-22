from functools import cache

class Solution:
    """
    兩數之間找合法數字 => 經典digit DP問題
    # i: 當前填到第幾個位置
    # isGreaterThanLowerbound, isLowerThanUpperbound: 當前放置是否超出上下限
    # leadingZero: 前導零
    # prev: 上一個位置填入的真實數字
    """
    def goodIntegers(self, l: int, r: int, k: int) -> int:
        low, high = str(l), str(r)
        while len(low) < len(high):
            low = "0" + low

        length = len(high)
        @cache
        def dfs(i, leadingZero, isGreaterThanLowerbound, isLowerThanUpperbound, prev):
            if i == length: return 1 if not leadingZero else 0 # 當我們擺脫前導零、才是有效數字

            start = 0 if isGreaterThanLowerbound else int(low[i])
            end = 10 if isLowerThanUpperbound else int(high[i])+1

            res = 0
            for d in range(start, end):
                isLeading = leadingZero and d == 0

                if prev == -1 or abs(d - prev) <= k:
                    res += dfs(i+1,
                        isLeading,
                        isGreaterThanLowerbound or d > int(low[i]),
                        isLowerThanUpperbound or d < int(high[i]),
                        prev if isLeading else d)
            return res
        return dfs(0, True, False, False, -1)