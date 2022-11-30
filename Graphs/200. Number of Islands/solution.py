class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0 <= row < ROWS and 0<= col < COLS:
                    if grid[row][col] == "1":
                        dfs(row, col)
            return True

        cnt = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0": continue
                if dfs(r, c): cnt += 1
        return cnt