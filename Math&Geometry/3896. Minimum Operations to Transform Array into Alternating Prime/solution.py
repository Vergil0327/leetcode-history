import math
from bisect import bisect_right

N = 101005
isPrime = [1]*N
isPrime[0] = isPrime[1] = 0
for i in range(2, int(math.sqrt(N)+1)):
    if isPrime[i]:
        for j in range(i*i, N, i):
            isPrime[j] = 0

primes = set([i for i in range(2, N) if isPrime[i]])
primeList = list(sorted(primes))

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if i%2 == 0 and nums[i] not in primes:
                j = bisect_right(primeList, nums[i])
                res += primeList[j] - nums[i]
            if i%2 == 1 and nums[i] in primes:
                while nums[i] in primes:
                    res += 1
                    nums[i] += 1
        return res