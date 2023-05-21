class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        queue = deque()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c):
            queue.append([r,c,0])
            grid[r][c] = -1
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if grid[row][col] == 0 or grid[row][col] == -1: continue
                dfs(row, col)

        foundFirstIsland = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                dfs(i, j)
                foundFirstIsland = True
                break
            if foundFirstIsland: break

        while queue:
            for _ in range(len(queue)):
                r, c, step = queue.popleft()

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] == -1: continue
                    if  grid[row][col] == 0:
                        queue.append([row, col, step+1])
                    else:
                        return step
                    grid[row][col] = -1
        return -1
                