class Solution:
    def latestDayToCross(self, ROW: int, COL: int, cells: List[List[int]]) -> int:
        parent = list(range(ROW*COL))

        def getID(r, c):
            return r*COL+c
        def getPos(id): # return (row, col)
            return id//COL, id%COL

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py

        n = len(cells)
        flooded = set([tuple((r-1, c-1)) for r, c in cells])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in flooded: continue
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row >= ROW or col < 0 or col >= COL: continue
                    if (row, col) in flooded: continue
                    union(getID(r,c), getID(row, col))

        for i in range(n-1, -1, -1):
            r, c = cells[i] # 1-based
            r, c = r-1, c-1
            flooded.remove((r, c))

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row >= ROW or col < 0 or col >= COL: continue
                if (row, col) in flooded: continue
                union(getID(r,c), getID(row, col))

            for col in range(COL):
                p = find(getID(ROW-1, col))
                row, _ = getPos(p)
                if row == 0: return i # 1-based, (i+1)-th day is still flooded, i-th day is the day
        return 0