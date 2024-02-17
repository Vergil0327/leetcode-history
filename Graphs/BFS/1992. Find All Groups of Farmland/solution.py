# BFS + floodfill
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []

        def BFS(x, y):
            queue = deque([(x, y)])
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]
            topleft = [x, y]
            botright = [x, y]
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if land[r][c] == 0: continue
                    land[r][c] = 0
                    botright[0] = max(botright[0], r)
                    botright[1] = max(botright[1], c)

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row < 0 or row >= m or col < 0 or col >= n: continue
                        if land[row][col] == 0: continue
                        if land[row][col] == 0: continue
                        queue.append((row, col))
            res.append([topleft[0], topleft[1], botright[0], botright[1]])

        for i in range(m):
            for j in range(n):
                if land[i][j] == 0: continue
                BFS(i, j)
        return res

# union-find
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        parent = list(range(m*n))
        rank = [1]*(m*n)

        def node(row, col):
            return row*n + col

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(i, j, x, y):
            px, py = find(node(i, j)), find(node(x, y))
            if px == py: return False

            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]
            return True

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0: continue

                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if x < 0 or x >= m or y < 0 or y >= n: continue
                    if land[x][y] == 0: continue
                    union(i, j, x, y)

        group = defaultdict(lambda: [m, n, -1, -1])
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0: continue
                p = find(node(i, j))
                group[p][0] = min(group[p][0], i)
                group[p][1] = min(group[p][1], j)
                group[p][2] = max(group[p][2], i)
                group[p][3] = max(group[p][3], j)
        
        return list(group.values())

# optimal
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0: continue

                r1, c1 = i, j
                r2, c2 = i, j
                while r2+1 < m and land[r2+1][c1] == 1:
                    r2 += 1
                while c2+1 < n and land[r1][c2+1] == 1:
                    c2 += 1
                res.append([r1,c1,r2,c2])
                
                # mark visited
                for x in range(r1, r2+1):
                    for y in range(c1, c2+1):
                        land[x][y] = 0
        return res