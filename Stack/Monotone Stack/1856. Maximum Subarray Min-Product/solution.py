class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prevSmaller = [-1] * n
        nextSmaller = [n] * n
        presum = [0]*(n+1)

        # 1 2 3 4 5 + 3
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

            presum[i+1] = presum[i]+nums[i]

        # 1 2 3 4 5 + 3 
        stack.clear()
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                nextSmaller[stack.pop()] = i

            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, nums[i] * (presum[nextSmaller[i]] - presum[prevSmaller[i]+1]))
        return res % 1_000_000_007
