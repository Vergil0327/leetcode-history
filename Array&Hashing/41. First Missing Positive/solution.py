class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums # to 1-based for convenience
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] >= n: # useless
                nums[i] = 0

        for i in range(n):
            while nums[i] != i:
                tmp = nums[i] # ! need to memorize nums[i]
                nums[i], nums[tmp] = nums[tmp], nums[i]
                if nums[i] == nums[nums[i]]: break # dead-loop, break and handle next position

        for i in range(1, n):
            if i != nums[i]: return i
        return n

# class Solution_TLE:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         seen = 0
#         for num in nums:
#             if num > 0:
#                 seen |= 1<<num
#         for i in range(1, int(2**31-1)):
#             if seen&1<<i == 0:
#                 return i