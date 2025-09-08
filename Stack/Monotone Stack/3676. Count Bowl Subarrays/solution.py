class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        prevGreater = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                prevGreater[i] = stack[-1]
            stack.append(i)

        nextGreater = [-1] * n
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            if nextGreater[i] != -1 and nextGreater[i] - i + 1 >= 3:
                res += 1
            if prevGreater[i] != -1 and i - prevGreater[i] + 1 >= 3:
                res += 1
        return res