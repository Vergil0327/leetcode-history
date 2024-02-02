class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if len(stack)%2 == 0: # find alternating positive sum
                if not stack or num > stack[-1]:
                    stack.append(num)
                elif num < stack[-1]:
                    stack[-1] = num
            else: # find alternating negative sum
                if num > stack[-1]:
                    stack[-1] = num
                elif num < stack[-1]:
                    stack.append(num)
        if stack and len(stack)%2 == 0:
            stack.pop()

        res = 0
        for i in range(len(stack)):
            if i%2 == 0:
                res += stack[i]
            else:
                res -= stack[i]
        return res
    