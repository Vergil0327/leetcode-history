class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        A, B = numerator, denominator
        if A%B == 0: return str(A//B)

        sign = 1
        if A < 0:
            A = abs(A)
            sign *= -1
        if B < 0:
            B = abs(B)
            sign *= -1

        res = "-" if sign < 0 else ""
        res += str(A // B) + "."
        
        remainder = A % B
        visited = {}

        i = 0
        while remainder != 0 and remainder not in visited:
            visited[remainder] = len(res)
            i += 1

            remainder *= 10
            res += str(remainder // B)
            remainder = remainder%B
        
        if remainder == 0:
            return res
        else:
            pos = visited[remainder]
            return f"{res[:pos]}({res[pos:]})"