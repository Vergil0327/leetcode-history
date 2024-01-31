class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rowsum = [[0]*(n+1) for _ in range(m+1)]
        colsum = [[0]*(n+1) for _ in range(m+1)]
        diag1 = [[0]*(n+2) for _ in range(m+2)]
        diag2 = [[0]*(n+2) for _ in range(m+2)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                rowsum[i][j] = rowsum[i][j-1] + grid[i-1][j-1]
                colsum[i][j] = colsum[i-1][j] + grid[i-1][j-1]
                diag1[i][j] = diag1[i-1][j-1] + grid[i-1][j-1]
                diag2[i][j] = diag2[i-1][j+1] + grid[i-1][j-1]

        res = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                for length in range(min(m-i, n-j), 0, -1):
                    SET = set()
                    SET.add(diag1[i+length][j+length] - diag1[i-1][j-1])
                    SET.add(diag2[i+length][j] - diag2[i-1][j+length+1])
                    for l in range(length+1):
                        SET.add(rowsum[i+l][j+length] - rowsum[i+l][j-1])
                        SET.add(colsum[i+length][j+l] - colsum[i-1][j+l])
                    if len(SET) == 1:
                        res = max(res, length+1)
        return res
