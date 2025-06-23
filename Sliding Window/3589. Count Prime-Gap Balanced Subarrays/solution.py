def generatePrimeUntil(n: int):
    isPrime = [0, 0] + [1] * (n-2)

    for i in range(2, int(sqrt(n))+1):
        if not isPrime[i]: continue
        # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
        for j in range(i*i, n, i):
            isPrime[j] = 0
    return isPrime

is_primes = generatePrimeUntil(50000+1)

# Solution using SortedList
from sortedcontainers import SortedList
class Solution1:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = r = res = 0
        sl = SortedList()
        indices = deque()
        while r < n:
            if is_primes[nums[r]]:
                sl.add(nums[r])
                indices.append(r)
            r += 1

            while len(sl) > 1 and sl[-1]-sl[0] > k:
                if is_primes[nums[l]]:
                    sl.remove(nums[l])
                    indices.popleft()
                l += 1

            res += (indices[-2]-l+1) if len(indices) > 1 else 0

        return res
 
# Optimized solution using deque
class Solution2:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l = r = res = 0
        mx = deque()
        mn = deque()
        indices = deque()
        while r < n:
            if is_primes[nums[r]]:
                while mx and nums[mx[-1]] < nums[r]:
                    mx.pop()
                mx.append(r)

                while mn and nums[mn[-1]] > nums[r]:
                    mn.pop()
                mn.append(r)

                indices.append(r)
            r += 1

            while len(indices) > 1 and mx and mn and nums[mx[0]]-nums[mn[0]] > k:
                if is_primes[nums[l]]:
                    if mx[0] == l:
                        mx.popleft()
                    if mn[0] == l:
                        mn.popleft()
                    indices.popleft()
                l += 1
            res += (indices[-2]-l+1) if len(indices) > 1 else 0

        return res
