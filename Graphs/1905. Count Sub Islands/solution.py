class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c):
            grid2[r][c] = 0
            isSubIsland = grid1[r][c] == 1
            for dr, dc in DIRS:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid2[row][col] == 1:
                    _, isValid = dfs(row, col)
                    if not isValid:
                        isSubIsland = False
            return 1 if isSubIsland else 0, isSubIsland


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] == 0: continue
                cnt, _ = dfs(r, c)
                res += cnt
        return res