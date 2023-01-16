# top-down
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dfs(r, c1, c2):
            if r == ROWS: return 0
            if c1 < 0 or c1 >= COLS or c2 < 0 or c2 >= COLS: return 0

            cherry = grid[r][c1]
            if c2 != c1: cherry += grid[r][c2]

            maxCherry = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    maxCherry = max(maxCherry, dfs(r+1, c1+i, c2+j))
            return maxCherry + cherry
        return dfs(0, 0,COLS-1) 

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[[-inf] * (COLS) for _ in range(COLS)] for _ in range(ROWS)]
        
        # base case
        dp[0][0][COLS-1] = grid[0][0] + grid[0][COLS-1]
        
        for r in range(1, ROWS):
            for c1 in range(COLS):
                for c2 in range(COLS):
                    for i in range(c1-1, c1+2):
                        for j in range(c2-1, c2+2):
                            if 0 <= i < COLS and 0 <= j < COLS:
                                if c1 != c2:
                                    dp[r][c1][c2] = max(dp[r][c1][c2], dp[r-1][i][j] + grid[r][c1] + grid[r][c2])
                                else:
                                    dp[r][c1][c2] = max(dp[r][c1][c2], dp[r-1][i][j] + grid[r][c1])

        res = 0
        for c1 in range(COLS):
            for c2 in range(COLS):
                res = max(res, dp[ROWS-1][c1][c2])
        return res