class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for num in nums:
            while stack and stack[-1][0] < num:
                stack.pop()
            if not stack or stack[-1][0] > num:
                stack.append([num, 0])
            stack[-1][1] += 1
            res += stack[-1][1]
        return res