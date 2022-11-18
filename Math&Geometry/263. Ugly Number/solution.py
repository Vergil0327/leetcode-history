class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        
        for p in [2, 3, 5]:
            while n%p == 0:
                n //= p
        return n == 1
        
#         # Count Primes, TLE
#         factors = [True] * (n+1)
#         for i in range(2, n+1):
#             if not factors[i]: continue

#             if i not in {2, 3, 5}: return False
#             if i < sqrt(n):
#                 for j in range(i*2, n+1, i):
#                     factors[j] = False
        return True