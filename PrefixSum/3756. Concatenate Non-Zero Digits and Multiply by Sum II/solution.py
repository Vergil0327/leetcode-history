
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 1_000_000_007
        n = len(s)

        digit_size = [0] * (n + 1) # count non-zero digits prefix
        digits = [0] * (n + 1) # concatenation prefix
        digitsum = [0] * (n + 1) # digit sum prefix

        length = 0  # number of non-zero digits so far
        for i in range(n):
            d = int(s[i])
            if d != 0:
                length += 1
                digits[length] = (digits[length-1] * 10 + d) % mod
                digitsum[length] = digitsum[length-1] + d
            digit_size[i+1] = length
        
        pow10 = [1] * (n + 1) # powers of 10
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % mod

        res = []
        for l, r in queries:
            a = digit_size[l]
            b = digit_size[r+1]

            length = b - a
            num = (digits[b] - digits[a] * pow10[length]) % mod
            sum_digits = digitsum[b] - digitsum[a]

            res.append((num * sum_digits) % mod)

        return res