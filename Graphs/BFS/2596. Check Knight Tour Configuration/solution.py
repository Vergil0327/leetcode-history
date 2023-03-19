class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0,0, 0)])

        dirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        
        while queue:
            for _ in range(len(queue)):
                r, c, step = queue.popleft()
                
                if grid[r][c] == step:
                    grid[r][c] = 0
                    
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS: continue
                    if grid[row][col] != step + 1: continue
                    
                    queue.append((row, col, step+1))

        return sum(map(sum, grid)) == 0
