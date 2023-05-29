class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c, prevR, prevC,ch, dist):
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if row == prevR and col == prevC: continue

                if (row,col) in dist:
                    if dist[(r,c)]+1 - dist[(row,col)] >= 4: return True
                    
                if grid[row][col] != ch: continue
                grid[row][col] = "#" # mark visited

                dist[(row, col)] = dist[(r,c)] + 1                
                if dfs(row, col, r, c, ch, dist): return True
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "#": continue
                distance = defaultdict(int)
                distance[(i,j)] = 1
                
                if dfs(i, j, -1, -1, grid[i][j], distance): return True
        return False
