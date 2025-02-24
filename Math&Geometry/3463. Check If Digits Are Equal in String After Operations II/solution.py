class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n == 2:
            return (s[0] == s[1])
        
        digits = list(map(int, s))
        N = n - 2
            
        def lucas_theorem(n: int, k: int, p: int):
            # n choose k mod p
            # can be represented with the per-"bit" product
            # see https://en.wikipedia.org/wiki/Lucas%27s_theorem
            product = 1
            while n != 0 or k != 0:
                n_dig = n % p
                k_dig = k % p
                if k_dig > n_dig:
                    return 0
                # small enough since we only have 5 and 2
                product *= math.comb(n_dig, k_dig)
                product %= p
                n //= p
                k //= p
            return product

        def binom_mod2(n, k):
            return lucas_theorem(n, k, 2)
        
        def binom_mod5(n, k):
            return lucas_theorem(n, k, 5)
        
        combine_map = {}
        for remainder in range(10):
            pair = (remainder % 2, remainder % 5)
            combine_map[pair] = remainder

        def binom_mod10(n, k):
            b2 = binom_mod2(n, k)
            b5 = binom_mod5(n, k)
            return combine_map[(b2, b5)]
        
        binom_table = [0]*(N+1)
        for k in range(N+1):
            binom_table[k] = binom_mod10(N, k)

        d0 = 0
        d1 = 0
        for m in range(N+1):
            coef = binom_table[m]
            d0 = (d0 + digits[m]*coef) % 10
            d1 = (d1 + digits[m+1]*coef) % 10    
        return (d0 == d1)
