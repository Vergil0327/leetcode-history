class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)

        nums = [[] for _ in range(k)]
        for i in range(n):
            nums[i%k].append(arr[i])

        res = 0
        for i in range(k):
            res += self.calculate(nums[i])
        return res

    def calculate(self, nums):
        n = len(nums)

        LIS = []
        for num in nums:
            j = bisect.bisect_right(LIS, num)
            if j == len(LIS):
                LIS.append(num)
            else:
                LIS[j] = num
        return n - len(LIS)
