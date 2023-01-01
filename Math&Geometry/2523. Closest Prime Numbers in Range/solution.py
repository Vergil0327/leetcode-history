class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = right+1
        isPrime = [0, 0] + [1] * (n-2)

        for i in range(2, int(math.sqrt(n))+1):
            if not isPrime[i]: continue
            for j in range(i*i, n, i):
                isPrime[j] = 0
        
        values = []
        for i in range(left, right+1):
            if isPrime[i]:
                values.append(i)

        gap = inf
        ans = None
        for i in range(len(values)-1):
            if values[i+1] - values[i] < gap:
                gap = values[i+1] - values[i]
                ans = [values[i], values[i+1]]
        
        return ans if ans else [-1, -1]
        