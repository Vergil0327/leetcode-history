class Solution:
    def minOperations(self, n: int) -> int:
        step = 0
        while n:
            while n&1 == 0:
                n >>= 1

            i = 0
            while (n>>i)&1:
                i += 1

            if i == 1:
                n>>= i
            else:
                n |= (1<<i)
                n >>= i

            step += 1

        return step

        
# 0b100111
# 0b101000
# 0b100000
# 0b110110
# 0b111000
# 0b1000000
