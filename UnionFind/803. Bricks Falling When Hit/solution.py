class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        # union-find
        toId = lambda r, c: r*n+c
        parent = list(range(m*n))
        rank = [1]*(m*n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            rowx, rowy = px//n, py//n
            if rowx < rowy:
                rank[px] += rank[py]
                parent[py] = px
            else:
                rank[py] += rank[px]
                parent[px] = py

        # remove hits
        for i, j in hits:
            if grid[i][j] == 0: continue
            grid[i][j] = -1 # mark removed bricks

        # group connected component after applying all the hits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == -1: continue
                for dx, dy in dirs:
                    row, col = i+dx, j+dy
                    if row<0 or row>=m or col<0 or col>=n: continue
                    if grid[row][col] == 0 or grid[row][col] == -1: continue
                    union(toId(i, j), toId(row, col))

        res = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                res.append(0)
                continue
            
            grid[r][c] = 1
            cnt = 0
            counted = set()
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row>=m or col<0 or col>=n: continue
                if grid[row][col] == 0 or grid[row][col] == -1: continue
                p = find(toId(row, col))
                pRow = p//n
                if pRow != 0 and p not in counted: # not solid
                    counted.add(p)
                    cnt += rank[p]
                union(toId(r, c), p)

            p = find(toId(r, c))
            if p//n == 0:
                res.append(cnt)
            else:
                res.append(0)
        return reversed(res)


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        # union-find
        toId = lambda r, c: r*n+c
        parent = list(range(m*n))
        rank = [1]*(m*n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return

            rowx, rowy = px//n, py//n
            if rowx < rowy:
                rank[px] += rank[py]
                parent[py] = px
            else:
                rank[py] += rank[px]
                parent[px] = py

        # remove hits
        for i, j in hits:
            if grid[i][j] == 0: continue
            grid[i][j] = -1 # mark removed bricks

        # group connected component after applying all the hits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == -1: continue
                for dx, dy in dirs:
                    row, col = i+dx, j+dy
                    if row<0 or row>=m or col<0 or col>=n: continue
                    if grid[row][col] == 0 or grid[row][col] == -1: continue
                    union(toId(i, j), toId(row, col))

        res = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                res.append(0)
                continue
            
            grid[r][c] = 1
            cnt = 0
            connectTop = False
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row>=m or col<0 or col>=n: continue
                if grid[row][col] == 0 or grid[row][col] == -1: continue
                
                p1, p2 = find(toId(row, col)), find(toId(r, c))
                if p1 == p2: continue

                pRow = p1//n
                if pRow == 0 or r == 0:
                    connectTop = True

                if pRow != 0: # not solid
                    cnt += rank[p1]
                union(p1, p2)

            res.append(cnt if connectTop else 0)
        return reversed(res)