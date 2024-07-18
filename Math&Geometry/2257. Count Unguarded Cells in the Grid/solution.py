class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[1]*n for _ in range(m)]
        for i, j in (walls + guards):
            grid[i][j] = -1
        
        for i, j in guards:
            x, y = i-1, j
            while x >= 0 and grid[x][y] != -1:
                grid[x][y] = 0
                x -= 1
            x, y = i+1, j
            while x < m and grid[x][y] != -1:
                grid[x][y] = 0
                x += 1
            x, y = i, j-1
            while y >= 0 and grid[x][y] != -1:
                grid[x][y] = 0
                y -= 1
            x, y = i, j+1
            while y < n and grid[x][y] != -1:
                grid[x][y] = 0
                y += 1
        
        return sum(grid[i][j] for i in range(m) for j in range(n) if grid[i][j] > 0)
