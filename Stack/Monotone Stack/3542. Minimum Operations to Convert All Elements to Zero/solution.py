class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0]
        res = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                res += 1
                stack.append(num)
        return res