class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 < num2: return -1

        for n in range(62):
            num = num1-n*num2
            if num.bit_count() <= n <= num:
                return n
        return -1
        
        
