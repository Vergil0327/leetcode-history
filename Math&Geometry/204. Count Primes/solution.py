
# Sieve of Eratosthenes
# we only neet to run sqrt(n) since number greater than sqrt(n) will be covered in nested loop
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [0, 0] + [1] * (n-2)

        for i in range(2, int(math.sqrt(n))+1):
            if not isPrime[i]: continue
            for j in range(i*i, n, i):
                isPrime[j] = 0
        return sum(isPrime)
