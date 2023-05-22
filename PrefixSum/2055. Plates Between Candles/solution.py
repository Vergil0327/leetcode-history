class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + (1 if s[i-1] == "*" else 0)

        candles = []
        for i, ch in enumerate(s):
            if ch == "|":
                candles.append(i)
        
        res = []
        for l, r in queries:
            i = bisect.bisect_left(candles, l)
            j = bisect.bisect_right(candles, r)-1
            if j < i:
                res.append(0)
            else:
                res.append(presum[candles[j]] - presum[candles[i]])
        return res