class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        direction = {
            (1,-1): (-1,-1),
            (-1,-1): (-1,1),
            (-1,1): (1,1),
            (1,1): (1,-1),
        }

        @lru_cache(None)
        def dfs(r, c, need, didTurn, curDirection):
            """
            need = 2 | 0
            next need = 2 if current is 0
                      = 0 if current is 2
                      = 2-need
            """
            step = 0

            row, col = r+curDirection[0], c+curDirection[1]
            if 0 <= row < m and 0 <= col < n and grid[row][col] == need:
                step = max(step, dfs(row, col, 2-need, didTurn, curDirection) + 1)

            if not didTurn: # turn 90 deg clockwise
                nextDirection = direction[curDirection]
                row, col = r+nextDirection[0], c+nextDirection[1]
                if 0 <= row < m and 0 <= col < n and grid[row][col] == need:
                    step = max(step, dfs(row, col, 2-need, True, nextDirection) + 1)
            return step

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    for curDirection in direction:
                        res = max(res, dfs(r, c, 2, False, curDirection)+1) # plus 1 for initial step `1`
        return res