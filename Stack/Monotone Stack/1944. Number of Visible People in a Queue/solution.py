class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        
        return res

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        
        res = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            cnt = 0
            while stack and heights[stack[-1]] <= heights[i]:
                cnt += 1
                stack.pop()
            if stack:
                cnt += 1

            res[i] = cnt
            stack.append(i)
        
        return res