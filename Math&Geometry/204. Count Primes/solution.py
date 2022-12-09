# Sieve of Eratosthenes
# we only neet to run sqrt(n) since number greater than sqrt(n) will be covered in nested loop
# time: O(n log log n)
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [0, 0] + [1] * (n-2)

        # take 12 as example
        # 12 = 2 × 6
        # 12 = 3 × 4
        # 12 = sqrt(12) × sqrt(12)
        # 12 = 4 × 3
        # 12 = 6 × 2
        # we can see that all the factors after sqrt(12) x sqrt(12) have been considered
        # thus, we only need to iterate until sqrt(n)+1 (strictly less than)
        for i in range(2, int(math.sqrt(n))+1):
            if not isPrime[i]: continue
            # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
            for j in range(i*i, n, i):
                isPrime[j] = 0
        return sum(isPrime)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0

        isPrime = [1]*n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, int(sqrt(n)+1)):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = 0
        return sum(isPrime)
