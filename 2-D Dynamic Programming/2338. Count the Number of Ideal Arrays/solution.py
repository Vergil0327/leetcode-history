# TLE for python
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7

        dp = [[0]*14 for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, 13+1):
                for t in range(j+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-t]) % mod

        # all the prime <= maxValue
        isPrime = [True] * (maxValue+1)
        isPrime[0] = isPrime[1] = False
        for num in range(2, int(sqrt(maxValue))+1):
            if not isPrime[num]: continue
            for j in range(num*num, maxValue+1, num):
                isPrime[j] = False
        primes = [num for num in range(2, maxValue+1) if isPrime[num]]

        res = 0
        for v in range(1, maxValue+1):
            ways = 1
            
            num = v
            for p in primes:
                count = 0
                while num > 1 and num%p == 0:
                    num //= p
                    count += 1
                
                ways = ways * dp[n][count] % mod
            res = (res + ways) % mod
        return res
    
# pass for python
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2261351/python3-freq-table/?orderBy=most_votes
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2261965/python-freq-table-solution-by-ye15-with-explanations/?orderBy=most_votes
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = maxValue
        freq = {x : 1 for x in range(1, maxValue+1)}
        for k in range(1, n): 
            temp = Counter()
            for x in freq: 
                for m in range(2, maxValue//x+1): 
                    ans += comb(n-1, k)*freq[x]
                    temp[m*x] += freq[x]
            freq = temp
            ans %= 1_000_000_007
        return ans 
    
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/solutions/2261280/python-arranging-primes-intro-to-combinatorics/
from math import sqrt

class Solution:
    def primesUpTo(self, n):
        primes = set(range(2, n + 1))
        for i in range(2, n):
            if i in primes:
                it = i * 2
                while it <= n:
                    if it in primes:
                        primes.remove(it)
                    it += i

        return primes

    def getPrimeFactors(self, n, primes):
        ret = {}
        sq = int(math.sqrt(n))

        for p in primes:
            if n in primes:
                ret[n] = 1
                break

            while n % p == 0:
                ret[p] = ret.get(p, 0) + 1
                n //= p

            if n <= 1:
                break

        return ret
        
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        ret = 0
        primes = self.primesUpTo(maxValue)
        
        for num in range(1, maxValue + 1):
            # find number of arrays that can end with num
            # for each prime factor, we can add it at any index i that we want
            pf = self.getPrimeFactors(num, primes)
            cur = 1
            for v in pf:
                count = pf[v]
                v = n
                # there are (n + 1) choose k ways to add k prime factors
                for add in range(1, count):
                    v *= (n + add)
                    v //= (add + 1)
                
                cur = (cur * v) % mod
                    
            ret = (ret + cur) % mod
                    
        return ret