class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        parent = list(range(m*n))
        rank = [1] * (m*n)
        key = lambda r, c: r * n + c

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row, col = r, c+1
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {1,3,5}:
                        union(key(r, c), key(row, col))
                    
                elif grid[r][c] == 2:
                    row, col = r+1, c
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {2,5,6}:
                        union(key(r,c), key(row, col))
                elif grid[r][c] == 3:
                    row, col = r+1, c
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {2,5,6}:
                        union(key(r,c), key(row, col))
                elif grid[r][c] == 4:
                    row, col = r, c+1
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {1,3,5}:
                        union(key(r, c), key(row, col))
                    row, col = r+1, c
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {2,5,6}:
                        union(key(r,c), key(row, col))
                elif grid[r][c] == 6:
                    row, col = r, c+1
                    if 0 <= row < m and 0 <= col < n and grid[row][col] in {1,3,5}:
                        union(key(r, c), key(row, col))

        return find(key(0, 0)) == find(key(m-1, n-1))
