class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        dist = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    dist[i][j] = 0
                    
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if dist[row][col] == -1:
                        dist[row][col] = dist[r][c] + 1
                        queue.append((row, col))

        maxHeap = [[-dist[0][0], 0, 0]]
        visited = [[0]*n for _ in range(m)]
        while maxHeap:
            wei, r, c  = heapq.heappop(maxHeap)

            if r == m-1 and c == n-1: return -wei
            if visited[r][c]: continue
            visited[r][c] = 1

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if visited[row][col]: continue
                heapq.heappush(maxHeap, [-min(-wei, dist[row][col]), row, col])
        return 0

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        dist = [[-1]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append((i, j))
                    dist[i][j] = 0
                    
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if dist[row][col] == -1:
                        dist[row][col] = dist[r][c] + 1
                        queue.append((row, col))

        def BFS(mid):
            s = [(0, 0)]
            seen = [[False]*n for i in range(n)]
            seen[0][0] = True
            while s:
                i, j = s.pop()
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < n and not seen[x][y] and dist[x][y] >= mid:
                        seen[x][y] = True
                        s.append((x, y))
            return seen[m-1][n-1]

        l, r = 0, dist[0][0]
        while l < r:
            mid = r - (r-l)//2

            if BFS(mid):
                l = mid
            else:
                r = mid-1
        return l