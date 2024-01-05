class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def BFS(start, visited):
            for r, c in start:
                visited[r][c] = 0
            queue = deque(start)
            step = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row<0 or row >= m or col < 0 or col >= n: continue
                        if grid[row][col] == 2: continue # wall
                        if visited[row][col] != inf: continue # visited
                        visited[row][col] = step+1
                        
                        if row == m-1 and col == n-1: continue
                        queue.append([row,col])
                step += 1

        person = [[inf]*n for _ in range(m)]
        fire = [[inf]*n for _ in range(m)]
        BFS([(0,0)], person) # person

        fires = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]  == 1:
                    fires.append([i,j])
        BFS(fires, fire)

        if person[m-1][n-1] == inf: return -1
        if fire[m-1][n-1] < person[m-1][n-1]: return -1
        if fire[m-1][n-1] == inf: return int(1e9)

        visited = [[0]*n for _ in range(m)]
        maxHeap = [[-fire[m-1][n-1], m-1, n-1]] # pq[i] = [t,row,col]: the last day `t` to reach (row,col)

        while maxHeap:
            t, r, c = heapq.heappop(maxHeap)
            if visited[r][c]: continue
            visited[r][c] = 1
            if r == 0 and c == 0: return -t

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row >= m or col < 0 or col >= n: continue
                if grid[row][col] == 2: continue # wall
                if visited[row][col]: continue # visited
                
                heapq.heappush(maxHeap, [-min(-t-1, fire[row][col]-1), row, col])
        return -1