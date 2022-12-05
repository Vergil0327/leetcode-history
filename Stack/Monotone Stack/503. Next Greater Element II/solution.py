from collections import defaultdict

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums.copy()
        arr.extend(nums[:-1])
        
        nextGreater = defaultdict(lambda: -1)
        
        stack = []
        for i, num in enumerate(arr):
            while stack and stack[-1][1] < num:
                j, _ = stack.pop()
                if j not in nextGreater:
                    nextGreater[j] = num # since value can be duplicate, we can't store value as key in nextGreater hashmap.
            stack.append((i, num))
        
        return [nextGreater[i] for i in range(len(nums))]

# use modulo to get circular index
class BetterSolution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                res[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return res