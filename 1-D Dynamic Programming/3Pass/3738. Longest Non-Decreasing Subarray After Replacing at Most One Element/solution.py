class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        premax = [1]
        n = len(nums)
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                premax.append(premax[-1]+1)
            else:
                premax.append(1)
        sufmax = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                sufmax[i] = sufmax[i+1]+1

        res = min(n, max(premax)+1)
        for i in range(1, n-1):
            if nums[i - 1] <= nums[i + 1]:
                res = max(res, premax[i - 1] + 1 + sufmax[i + 1])

        return res