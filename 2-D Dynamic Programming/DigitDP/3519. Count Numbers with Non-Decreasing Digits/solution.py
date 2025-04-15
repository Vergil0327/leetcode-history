class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        def parse(num: int, base: int) -> str:
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return "".join(reversed(digits))
        L, R = parse(int(l), b), parse(int(r), b)

        while len(L) < len(R):
            L = "0" + L
        
        n = len(L)
        mod = 10**9+ 7

        @cache
        def dfs(i, greaterThanLow, lowerThanHigh, leadingZero, prev):
            if i >= n: return 1
            start = 0 if greaterThanLow else int(L[i])
            end = b if lowerThanHigh else int(R[i])+1

            res = 0
            for d in range(start, end):
                if d < prev: continue
                res += dfs(i+1,
                    greaterThanLow or d > int(L[i]),
                    lowerThanHigh or d < int(R[i]),
                    leadingZero and d == 0,
                    d)
                res %= mod
            return res
        return dfs(0, False, False, True, -1)
