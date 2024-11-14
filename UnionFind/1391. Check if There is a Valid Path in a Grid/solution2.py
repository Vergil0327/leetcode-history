class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = [
            [[0, 0] , [0, 0]], # 0th is a placeholder for index shift
            [[0, -1], [0, 1]],
            [[-1, 0], [1, 0]],
            [[0, -1], [1, 0]],
            [[0, 1], [1, 0]],
            [[0, -1], [-1, 0]],
            [[0, 1], [-1, 0]]
        ]
        queue = [(0, 0)]
        seen = [[False] * n for _ in range(m)]
        for r, c in queue:
            if seen[r][c]: continue
            seen[r][c] = True

            for dr, dc in dirs[grid[r][c]]:
                row, col = dr + r, dc + c
                if not 0 <= row < m or not 0 <= col < n:
                    continue

                # check if two section are connected
                for backDr, backDc in dirs[grid[row][col]]:
                    if row + backDr == r and col + backDc == c:
                        queue.append((row, col))
                        break
        return seen[m - 1][n - 1]