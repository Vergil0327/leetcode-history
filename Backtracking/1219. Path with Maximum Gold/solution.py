class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        res = 0
        def dfs(r, c):
            if grid[r][c] == 0: return 0
            res = 0
            v = grid[r][c]
            grid[r][c] = 0
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row>=m or col<0 or col>=n: continue
                res = max(res, dfs(row, col))
            grid[r][c] = v
            return res + v

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i,j))
        return res
