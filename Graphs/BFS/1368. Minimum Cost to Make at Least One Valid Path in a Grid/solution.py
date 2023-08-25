class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        startingPoints = deque()
        queue = deque([(0,0)])
        visited = [[0]*n for _ in range(m)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m-1 and c == n-1: return 0
                if visited[r][c]: continue
                startingPoints.append([r,c])
                visited[r][c] = 1

                dr, dc = dirs[grid[r][c]-1]
                row, col = r+dr, c+dc
                if 0 <= row < m and 0 <= col < n:
                    queue.append([row, col])

        def canReach(r, c):
            # if r < 0 or r >= m or c < 0 or c >= n: return set()
            # if visited[r][c]: return set()
            # visited[r][c] = 1
            
            # dr, dc = dirs[grid[r][c]-1]
            # return canReach(r+dr, c+dc) | set([(r,c)])

            paths = []
            while 0 <= r < m and 0 <= c < n and not visited[r][c]:
                visited[r][c] = 1
                paths.append([r, c])

                dr, dc = dirs[grid[r][c]-1]
                r, c = r+dr, c+dc
            return paths

        cost = 0
        while startingPoints:
            cost += 1
            for _ in range(len(startingPoints)):
                r, c = startingPoints.popleft()

                for dr,dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if visited[row][col]: continue
                    
                    nexts = canReach(row, col)
                    for nxt in nexts:
                        if nxt[0] == m-1 and nxt[1] == n-1: return cost
                        startingPoints.append(nxt)

        return cost
