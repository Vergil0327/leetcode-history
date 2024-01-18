class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        nextSmaller = [n]*n
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                nextSmaller[stack.pop()] = i
            stack.append(i)

        prevSmaller = [-1]*n
        stack = []
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                stack.pop()

            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            if nums[i] * (size := nextSmaller[i]-prevSmaller[i]-1) > threshold:
                return size
        return -1    