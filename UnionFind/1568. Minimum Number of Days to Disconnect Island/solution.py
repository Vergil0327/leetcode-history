class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def UnionFindCount():
            parent = list(range(m*n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 0:
                        parent[r*n+c] = -1
                        continue

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row < 0 or row >= m or col < 0 or col >= n: continue
                        if grid[row][col] == 0: continue
                        
                        px, py = find(r*n+c), find(row*n+col)
                        if px == py: continue
                        if px <= py:
                            parent[py] = px
                        else:
                            parent[px] = py

            return len(set(find(p) for p in parent if p != -1))
        
        island = UnionFindCount()
        if island != 1: return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue

                grid[i][j] = 0
                if UnionFindCount() != 1:
                    return 1
                grid[i][j] = 1
        return 2
