# O(K+N*log(K))
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ptrs = [0]*len(primes)
        nums = [1]
        minHeap = []
        for i, prime in enumerate(primes):
            heapq.heappush(minHeap, [prime * nums[ptrs[i]], i])

        while len(nums)<n:
            minPrime = minHeap[0][0]
            nums.append(minPrime)

            while minHeap and minHeap[0][0] == minPrime:
                _, idx = heapq.heappop(minHeap)
                ptrs[idx] += 1
                heapq.heappush(minHeap, [nums[ptrs[idx]] * primes[idx], idx])
        return nums[n-1]

# O(N*2K)
class SolutionTLE:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ptrs = [0]*len(primes)
        nums = [1]

        while len(nums)<n:
            minUgly = float("inf")
            for i, ptr in enumerate(ptrs):
                minUgly = min(minUgly, nums[ptr] * primes[i])
            nums.append(minUgly)

            for i, ptr in enumerate(ptrs):
                if nums[ptr] * primes[i] == minUgly:
                    ptrs[i] += 1
        return nums[n-1]