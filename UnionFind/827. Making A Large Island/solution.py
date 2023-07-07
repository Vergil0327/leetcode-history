class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = list(range(m*n))
        rank = [1] * (m*n)

        def key(row, col):
            return row*n+col

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] == 0: continue

                    a = find(key(r, c))
                    b = find(key(row, col))
                    if a == b: continue
                    if rank[a] >= rank[b]:
                        parent[b] = a
                        rank[a] += rank[b]
                    else:
                        parent[a] = b
                        rank[b] += rank[a]

        res = max(rank) # default value is maximum of un-union island
        for r in range(m):
            for c in range(n):
                if grid[r][c]: continue

                exist = set()
                area = 1 # grid[r][c] + island in 4 directions
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] == 0: continue
                    x = find(key(row, col))
                    if x in exist: continue
                    exist.add(x)
                    area += rank[x]
                res = max(res, area)
        return res
