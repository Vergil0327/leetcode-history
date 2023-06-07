class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)

        mat = [[0]*cols for _ in range(rows)]

        def dfs(i, j):
            if i == rows: return
            if j == cols: return dfs(i+1, 0)

            mat[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= mat[i][j]
            colSum[j] -= mat[i][j]
            dfs(i, j+1)
        dfs(0, 0)
        return mat
    
# optimization
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)

        mat = [[0]*cols for _ in range(rows)]

        def dfs(i, j):
            if i >= rows and j >= cols: return
            if i >= rows:
                mat[rows-1][j] = colSum[j]
                colSum[j] = 0
                return dfs(i, j+1)
            if j >= cols:
                mat[i][cols-1] = rowSum[i]
                rowSum[i] = 0
                return dfs(i+1, j)

            mat[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= mat[i][j]
            colSum[j] -= mat[i][j]
            
            if rowSum[i] == colSum[j]:
                return dfs(i+1, j+1)
            elif rowSum[i] > colSum[j]:
                return dfs(i, j+1)
            else:
                return dfs(i+1, j)
        dfs(0, 0)

        return mat
