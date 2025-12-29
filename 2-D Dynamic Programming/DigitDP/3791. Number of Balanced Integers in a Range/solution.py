"""
在兩數範圍內, 尋找合法digits數目
=> 直覺想到digit DP

而且還是最典型的那種, 僅需要考慮偶數位跟奇數位的差為0即可
"""

class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        low = str(low)
        high = str(high)
        while len(low) < len(high):
            low = "0" + low
        
        @cache
        def dfs(i, lowerThanHigh, higherThanLow, balance):
            if i >= len(high):
                return int(balance == 0)
            start = 0 if higherThanLow else int(low[i])
            end = 10 if lowerThanHigh else (int(high[i]))+1

            res = 0
            for d in range(start, end):
                res += dfs(i+1,
                    lowerThanHigh or d < int(high[i]),
                    higherThanLow or d > int(low[i]),
                    balance + pow(-1, i) * d)
            return res

        return dfs(0, False, False, 0)