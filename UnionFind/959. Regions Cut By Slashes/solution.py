class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(n*n*4))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px <= py:
                    parent[py] = px
                else:
                    parent[px] = py

        # union splitted cells
        for i in range(n):
            for j in range(n):
                cell1 = (i*n+j)*4+0
                cell2 = (i*n+j)*4+1
                cell3 = (i*n+j)*4+2
                cell4 = (i*n+j)*4+3
                
                if grid[i][j] == "/":
                    # cell2 | cell3
                    union(cell2, cell3)
                    
                    # cell1 | cell4
                    union(cell1, cell4)
                elif grid[i][j] == " ":
                    # union all together
                    union(cell1, cell2)
                    union(cell2, cell3)
                    union(cell3, cell4)
                else:
                    union(cell1, cell2)
                    union(cell3, cell4)

        # # union cell row-by-row, column-by-column
        for i in range(n):
            for j in range(n):
                cell1 = (i*n+j)*4+0
                cell2 = (i*n+j)*4+1
                cell3 = (i*n+j)*4+2
                cell4 = (i*n+j)*4+3
                if i > 0:
                    prev3 = ((i-1)*n+j)*4+2
                    union(cell1, prev3)
                if j > 0:
                    prev2 = (i*n+(j-1))*4+1
                    union(cell4, prev2)

        groups = set()
        for p in map(find, parent):
            groups.add(p)

        return len(groups)

# Concise
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(n*n*4))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px <= py:
                    parent[py] = px
                else:
                    parent[px] = py

        # union splitted cells
        for i in range(n):
            for j in range(n):
                cell1 = (i*n+j)*4+0
                cell2 = (i*n+j)*4+1
                cell3 = (i*n+j)*4+2
                cell4 = (i*n+j)*4+3
                
                if grid[i][j] == "/":
                    # cell2 | cell3
                    union(cell2, cell3)
                    
                    # cell1 | cell4
                    union(cell1, cell4)
                elif grid[i][j] == " ":
                    # union all together
                    union(cell1, cell2)
                    union(cell2, cell3)
                    union(cell3, cell4)
                else:
                    union(cell1, cell2)
                    union(cell3, cell4)
                
                # union cell row-by-row, column-by-column
                if i > 0:
                    prev3 = ((i-1)*n+j)*4+2
                    union(cell1, prev3)
                if j > 0:
                    prev2 = (i*n+(j-1))*4+1
                    union(cell4, prev2)

        groups = set()
        for p in map(find, parent):
            groups.add(p)

        return len(groups)
