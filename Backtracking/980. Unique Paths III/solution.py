class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, steps):
            if grid[r][c] == 2:
                if steps == 0: return 1
                return 0

            if grid[r][c] == -1: return 0
            ori = grid[r][c]
            grid[r][c] = -1 # mark visited

            path = 0
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if not (0 <= row < ROWS and 0 <= col < COLS): continue
                if grid[row][col] == -1: continue
                path += dfs(row, col, steps - 1)

            grid[r][c] = ori # backtracking

            return path

        steps = 0
        starting = None
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 or grid[r][c] == 2:
                    steps += 1
                elif grid[r][c] == 1:
                    starting = (r, c)

        return dfs(starting[0], starting[1], steps)