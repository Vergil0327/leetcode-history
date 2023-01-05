class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        currMin = inf
        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack:
                minUntilNow = stack[-1][1] # nums[i]
                if num > minUntilNow: return True
            
            stack.append([num, currMin])
            currMin = min(currMin, num)

        return False