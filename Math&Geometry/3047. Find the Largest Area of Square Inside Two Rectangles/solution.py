class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:        
        arr = list(zip(bottomLeft, topRight))
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                (r1, c1), (r2, c2) = arr[i]
                (x1, y1), (x2, y2) = arr[j]
                
                
                x = [max(r1, x1), max(c1, y1)]
                y = [min(r2, x2), min(c2, y2)]
                res = max(res, max(0, min(y[0]-x[0], y[1]-x[1]))**2)
        
        return res
