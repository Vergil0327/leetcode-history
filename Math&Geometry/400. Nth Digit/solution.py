class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10: return n
        def count(d):
            return d*(10**d) - d*(10**(d-1))
        
        digits = 1
        cnt = count(digits)
        while n > cnt:
            n -= cnt
            digits += 1
            cnt = count(digits)

        i, j = n//digits, n%digits
        if j != 0:
            num = 10 ** (digits-1) + i
            return int(str(num)[j-1])
        else:
            num = 10 ** (digits-1) + i - 1
            return int(str(num)[-1])