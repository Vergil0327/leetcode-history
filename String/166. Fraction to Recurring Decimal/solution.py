class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator == 0: return str(numerator//denominator)

        diffSign = (numerator > 0) ^ (denominator > 0)
        res = "-" if diffSign else "" # handle sign
        
        A, B = abs(numerator), abs(denominator)
        res += str(A // B) + "."
        
        remainder = A % B
        visited = {}

        while remainder != 0 and remainder not in visited:
            visited[remainder] = len(res)

            remainder *= 10
            res += str(remainder // B)
            remainder = remainder%B
        
        if remainder == 0:
            return res
        else:
            pos = visited[remainder]
            return f"{res[:pos]}({res[pos:]})"