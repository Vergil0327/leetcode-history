class Solution:
    def baseNeg2(self, n: int) -> str:
        res = ""
        while n != 0:
            mod = n%(-2)
            n //= -2

            if mod < 0:
                mod += 2
                n += 1
            res = str(mod) + res
        return res if res else "0"