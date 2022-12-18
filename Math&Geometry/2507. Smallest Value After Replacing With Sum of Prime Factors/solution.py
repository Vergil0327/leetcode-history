# straightforward solution
class Solution:
    def smallestValue(self, n: int) -> int:
        isPrime = [True] * (n+1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(sqrt(n))+1):
            if not isPrime[i]: continue
            for j in range(i*i, n+1, i):
                isPrime[j] = False

        arr = [i for i, isPri in enumerate(isPrime) if isPri]
        while not isPrime[n]:
            original = n
            primes = []
            for num in arr:
                while n%num == 0:
                    primes.append(num)
                    n //= num
                    if isPrime[n]:
                        primes.append(n)
                        break
                if isPrime[n]:
                    break

            n = sum(primes)
            if n == original: break

        return n

# Concise
class Solution:
    def smallestValue(self, n: int) -> int:
        def getPrimeSum(n):
            total = 0
            for i in range(2, n+1):
                while n%i == 0:
                    total += i
                    n //= i
            return total

        while n != (nxt := getPrimeSum(n)):
            n = nxt
        return n
