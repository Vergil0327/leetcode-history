# from math import comb
# class Solution:
#     def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
#         left = pos
#         right = n - pos - 1
#         mod = 10**9 + 7
        
#         res = 0
#         for i in range(k+1):
#             res += comb(left, i) * comb(right, k-i)
#             res %= mod

#         return (res * 2)%mod # person at pos can choose either L or R

class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        MOD = 10**9 + 7

        fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        # factorial
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # fast power
        def power(a, b):
            res = 1
            while b:
                if b & 1:
                    res = res * a % MOD
                a = a * a % MOD
                b >>= 1
            return res

        # inverse factorial
        inv[n] = power(fact[n], MOD - 2)
        for i in range(n - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % MOD

        def comb(n, r):
            return fact[n] * inv[r] % MOD * inv[n - r] % MOD

        left = pos
        right = n - pos - 1
        
        res = 0
        # res += comb(left, i) * comb(right, k - i)
        # => valid range of i: considering `left`: [k-right, min(left, k)] and k-right >= 0
        for i in range(max(0, k - right), min(left, k) + 1):
            res = (res + comb(left, i) * comb(right, k - i)) % MOD

        return (res * 2) % MOD  # person at pos can choose either L or R