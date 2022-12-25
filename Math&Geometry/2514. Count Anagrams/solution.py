from collections import Counter
from math import factorial

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 1000000007
        res = 1
        for word in s.split():
            counter = Counter(word)

            perms = factorial(len(word))
            for freq in counter.values():
                perms //= factorial(freq)

            res *= (perms % MOD)

        return res % MOD

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 1000000007
        n = len(s)

        fact = [1] * (n+1)
        invFact = [1] * (n+1)
        for num in range(1, n+1):
            fact[num] = fact[num-1] * num % MOD
            invFact[num] = invFact[num-1] * pow(num, MOD-2, MOD) % MOD
        
        res = 1
        for word in s.split():
            res *= fact[len(word)]
            for freq in Counter(word).values():
                res *= invFact[freq]
            res %= MOD
        return res

class Solution: 
    def countAnagrams(self, s: str) -> int:
        n = len(s)
        mod = 1_000_000_007
        inv = [1]*(n+1)
        fact = [1]*(n+1)
        ifact = [1]*(n+1)
        for x in range(1, n+1): 
            if x >= 2: inv[x] = mod - mod//x * inv[mod % x] % mod 
            fact[x] = fact[x-1] * x % mod 
            ifact[x] = ifact[x-1] * inv[x] % mod 

        ans = 1
        for word in s.split(): 
            ans *= fact[len(word)]
            for x in Counter(word).values(): ans *= ifact[x]
            ans %= mod 
        return ans 