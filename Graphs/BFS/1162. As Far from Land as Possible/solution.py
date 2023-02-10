class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        queue = deque()        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))

        dist = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row>=ROWS or col<0 or col >= COLS: continue
                    if grid[row][col] == 1: continue
                    grid[row][col] = 1
                    queue.append((row, col))
            dist += 1
        return dist if dist != 0 else -1             

# 1 0 0 0 1
# 0 0 0 0 0
# 1 0 0 0 1

# 1 1 0 1 1
# 1 0 0 0 1
# 1 1 0 1 1

# 1 1 1 1 1
# 1 1 0 1 1
# 1 1 1 1 1

# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1