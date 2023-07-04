class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        res = 0
        histogram = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    histogram[j] += 1
                else:
                    histogram[j] = 0

            h = sorted(histogram, reverse=True)
            # X   X                           X       X
            # X X X                           X X     X
            # X X   X X -> h = [3,2,1,1,0] -> X X X X 
            height = inf
            for k in range(n):
                height = min(height, h[k])
                width = (k+1)
                res = max(res, height * width)
        return res