from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ISLAND, WATER = 1, 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c):
            nonlocal key
            grid[r][c] = WATER

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == ISLAND:
                    key += f"[+{dr},{dc}]"
                    dfs(row, col)
                    key += f"[-{dr},{dc}]"

        # we can use relative coordinate or serialize recursion tree to get distinct island
        distinct = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ISLAND:
                    key = ""
                    dfs(r, c)
                    distinct.add(key)
        return len(distinct)
