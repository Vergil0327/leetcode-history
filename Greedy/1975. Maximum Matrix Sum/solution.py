class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = negative_cnt = 0
        mn = int(1e6)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negative_cnt += 1
                
                mn = min(mn, abs(matrix[i][j]))
                res += abs(matrix[i][j])

        if negative_cnt%2 == 0:
            return res
        else:
            return res-mn*2
