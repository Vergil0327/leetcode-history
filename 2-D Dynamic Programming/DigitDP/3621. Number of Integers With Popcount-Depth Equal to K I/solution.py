class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0: return 1
        if k == 1:
            return len(bin(n)[2:]) - 1 # excluding 1. ex. "10", "100", "1000", ...

        high = bin(n)[2:]
        low = "1"
        while len(low) < len(high):
            low = "0" + low

        m = len(high)
        depth = [0] * 51
        for i in range(2, 51):
            depth[i] = depth[i.bit_count()]+1

        valid = set([i for i in range(1, 51) if depth[i] == k-1])

        @cache
        def dfs(i, lowerThanHigh, higherThanLow, ones):
            if i >= m: return int(ones in valid)

            start = 0 if higherThanLow else int(low[i])
            end = 2 if lowerThanHigh else int(high[i])+1

            res = 0
            for d in range(start, end):
                res += dfs(i+1, lowerThanHigh or d < int(high[i]), higherThanLow or d > int(low[i]), ones + int(d==1))

            return res

        return dfs(0, False, False, 0)