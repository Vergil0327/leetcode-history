class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x = sorted([[ax1, ax2], [bx1, bx2]])
        y = sorted([[ay1, ay2], [by1, by2]])
        
        maxArea = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1)
        if x[0][1] < x[1][0] or y[0][1] < y[1][0]: # no overlapping
            return maxArea


        xside = min(x[0][1],x[1][1]) - max(x[0][0], x[1][0])
        yside = min(y[0][1],y[1][1]) - max(y[0][0], y[1][0])
        return maxArea - xside * yside