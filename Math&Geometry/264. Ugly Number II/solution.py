# min heap: 3N*log(3N)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]

        minH = [2, 3, 5]
        while len(nums) < n:
            num = heapq.heappop(minH)
            while minH and minH[0] == num:
                heapq.heappop(minH)
            nums.append(num)
            heapq.heappush(minH, num*2)
            heapq.heappush(minH, num*3)
            heapq.heappush(minH, num*5)
        return nums[n-1]

# O(N)
class OptimizedSolution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i = j = k = 0

        while len(nums) < n:
            nums.append(min(min(nums[i]*2, nums[j]*3), nums[k]*5))
            if nums[-1] == nums[i]*2:
                i += 1
            if nums[-1] == nums[j]*3:
                j += 1
            if nums[-1] == nums[k]*5:
                k += 1

        return nums[n-1]