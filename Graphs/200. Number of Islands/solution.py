class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        cnt = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r, c):
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col] == "1":
                    grid[row][col] = "0"
                    dfs(row, col)
            return 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0": continue
                cnt += dfs(r, c)
        return cnt
        

# Union-Find
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        parent = [i for i in range(ROWS*COLS)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            
            parent[py] = px
        
        def key(r,c):
            return r*COLS+c
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == "1":
                            union(key(r,c), key(row, col))
        
        count = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count.add(find(key(r,c)))
        return len(count)