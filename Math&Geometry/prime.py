from math import sqrt

def generatePrimeUntil(n: int):
    isPrime = [0, 0] + [1] * (n-2)

    for i in range(2, int(sqrt(n))+1):
        if not isPrime[i]: continue
        # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
        for j in range(i*i, n, i):
            isPrime[j] = 0
