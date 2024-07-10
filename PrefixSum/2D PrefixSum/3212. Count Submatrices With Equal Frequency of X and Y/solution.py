class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        grid = [[1 if grid[i][j] == "X" else -1 if grid[i][j] == "Y" else 0 for j in range(n)] for i in range(m)]

        presum2D = [[0]*(n+1) for _ in range(m+1)]
        presumX = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        for i in range(m):
            for j in range(n):
                presum2D[i+1][j+1] = presum2D[i+1][j] + presum2D[i][j+1] + grid[i][j] - presum2D[i][j]
                presumX[i+1][j+1] = presumX[i+1][j] + presumX[i][j+1] + int(grid[i][j] == 1) - presumX[i][j]

                if presum2D[i+1][j+1] == 0 and presumX[i+1][j+1] > 0:
                    res += 1

        return res