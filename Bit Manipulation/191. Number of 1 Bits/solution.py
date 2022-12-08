class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for _ in range(32):
            cnt += n&1
            n >>= 1
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        # example: n = 3 (11)
        #  11
        # &10
        # =10
        # &01
        # =00
        cnt = 0
        while n > 0:
            n &= n-1
            cnt += 1
        return cnt