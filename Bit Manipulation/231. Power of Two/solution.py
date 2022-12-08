# Observation
# 001
# 010
# 100
# we can see that it must exist only 1 bit for 2^x
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def countOneBit(n) -> int:
            cnt = 0
            while n > 0:
                n &= n-1
                cnt += 1
            return cnt
        return countOneBit(n) == 1

# Follow-Up
# from solution above
# countOneBit(n) == 1 means only one iteration
# we can just check n& n-1 == 0
# ! but be careful of edge case: 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & n-1 == 0
