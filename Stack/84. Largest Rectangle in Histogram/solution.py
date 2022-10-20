# https://www.youtube.com/watch?v=zx5Sw9130L0&t=1s
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, height)
        
        maxRec = 0
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                j, hei = stack.pop()
                maxRec = max(maxRec,(i-j)*hei)
                start = j # extend back
            stack.append((start,h))
            
        for i, h in stack:
            maxRec = max(maxRec, h*(len(heights)-i))
        
        return maxRec