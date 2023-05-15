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