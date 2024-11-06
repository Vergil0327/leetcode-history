class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        horizontalCuts.sort()

        verticalCuts.extend([0, w])
        verticalCuts.sort()
        
        m, n = len(horizontalCuts), len(verticalCuts)

        maxHeight = 0
        for i in range(m-1):
            height = horizontalCuts[i+1] - horizontalCuts[i]
            maxHeight = max(maxHeight, height)

        maxWidth = 0
        for j in range(n-1):
            width = verticalCuts[j+1] - verticalCuts[j]
            maxWidth = max(maxWidth, width)
        return maxHeight * maxWidth % 1_000_000_007