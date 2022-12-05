class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        LOWER, UPPER = int(-2**31), int(2**31 - 1)
        isNegtive = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a, b = abs(dividend), abs(divisor)
        
        quotient = 0
        base = 1
        while a >= abs(divisor):
            if a < b:
                b = abs(divisor)
                base = 1
                continue
            a -= b
            quotient += base
            b <<= 1
            base <<= 1
        

        if isNegtive:
            if -quotient < LOWER:
                return LOWER
            else:
                return -quotient
        else:
            if quotient > UPPER:
                return UPPER
            else:
                return quotient

class Solution_Optimized:
    def divide(self, dividend: int, divisor: int) -> int:
        LOWER, UPPER = int(-2**31), int(2**31 - 1)
        isNegtive = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a, b = abs(dividend), abs(divisor)
        
        quotient = 0
        while a >= abs(divisor):
            candidate = b
            base = 1
            while candidate<<1 < a:
                candidate <<= 1
                base <<= 1
            a -= candidate
            quotient += base

        if isNegtive:
            if -quotient < LOWER:
                return LOWER
            else:
                return -quotient
        else:
            if quotient > UPPER:
                return UPPER
            else:
                return quotient