class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            if not stack:
                stack.append(num)
            else:
                remain = n-1-i
                while stack and stack[-1] > num and len(stack)+remain >= k:
                    stack.pop()
                stack.append(num)
        return stack[:k]