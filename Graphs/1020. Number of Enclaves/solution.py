class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c):
            grid[r][c] = 0

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == 1:
                    dfs(row, col)

        for r in range(ROWS):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][COLS-1] == 1:
                dfs(r, COLS-1)
        for c in range(COLS):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[ROWS-1][c] == 1:
                dfs(ROWS-1, c)
        return sum(map(sum, grid))