class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def flood(r, c):
            grid[r][c] = 1
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == 0:
                    flood(row, col)
            return 1

        for r in range(ROWS):
            if grid[r][0] == 0:
                flood(r, 0)
            if grid[r][COLS-1] == 0:
                flood(r, COLS-1)
        for c in range(COLS):
            if grid[0][c] == 0:
                flood(0, c)
            if grid[ROWS-1][c] == 0:
                flood(ROWS-1, c)

        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    total += flood(r, c)
        return total