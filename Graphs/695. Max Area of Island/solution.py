class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c):
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == 1:
                    area += dfs(row, col)
            return area 

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: continue
                res = max(res, dfs(r, c))
        return res