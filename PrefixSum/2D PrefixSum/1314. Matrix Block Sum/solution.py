# O(n^3)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        answer = [[0]*n for _ in range(m)]
        presum = []
        for row in mat:
            presum.append(list(accumulate(row, initial=0)))
        
        for i in range(m):
            for j in range(n):
                for row in range(max(0, i-k), min(m, i+k+1)):
                    answer[i][j] += presum[row][min(n, j+k+1)] - presum[row][max(0, j-k)]
        return answer

# O(n^2)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        presum2D = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):                
                presum2D[i+1][j+1] = mat[i][j] + presum2D[i][j+1] + presum2D[i+1][j] - presum2D[i][j]

        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i-k), min(m, i+k+1)
                c1, c2 = max(0, j-k), min(n, j+k+1)
                answer[i][j] = presum2D[r2][c2] - presum2D[r2][c1] - presum2D[r1][c2] + presum2D[r1][c1]

        return answer
