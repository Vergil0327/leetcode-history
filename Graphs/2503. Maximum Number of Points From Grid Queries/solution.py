class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:        
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        minheap = [(grid[0][0], 0, 0)]
        grid[0][0] = 0 # floodfill as visited set
        
        order = []
        while minheap:
            currVal, r, c = heapq.heappop(minheap)
            order.append(currVal)
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and grid[row][col]:
                    heapq.heappush(minheap, (grid[row][col], row, col))
                    grid[row][col] = 0
        
        maxUntil = -inf
        for i in range(len(order)):
            maxUntil = max(maxUntil, order[i])
            order[i] = maxUntil
        
        res = []
        for q in queries:
            i = bisect.bisect_left(order, q)
            res.append(i)
        return res

# BFS + Priority Queue
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:        
        ROWS, COLS = len(grid), len(grid[0])

        pq = [[grid[0][0], 0, 0]] # [grid, row, col]
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        ans = [0] * len(queries)
        count = 0
        sortedQueries = sorted([query, i] for i, query in enumerate(queries))

        for query, i in sortedQueries:
            while pq and pq[0][0] < query:
                _, r, c = heapq.heappop(pq)
                count += 1
                grid[r][c] = 0
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row >= ROWS or col<0 or col >= COLS or grid[row][col] == 0: continue
                    heapq.heappush(pq, [grid[row][col], row, col])
                    grid[row][col] = 0
            ans[i] = count
        return ans

# Union-Find
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:        
        ROWS, COLS = len(grid), len(grid[0])

        # turn 2-D array into 1-D row-based array
        parent = [i for i in range(ROWS * COLS + COLS)]
        rank = [1] * (ROWS * COLS + COLS)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            parent[py] = px
            rank[px] += rank[py]

        # sort node in increasing order to help us find each query's answer
        nodes = []
        for r in range(ROWS):
            for c in range(COLS):
                nodes.append([grid[r][c], r, c])
        nodes.sort()

        # find answer in increasing order
        sortedQueries = sorted([[q, i] for i, q in enumerate(queries)])
        
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        ans = [0] * len(queries)
        visited = [0] * (ROWS*COLS+COLS)
        idx = 0
        for query, idxQ in sortedQueries:
            while idx < ROWS * COLS and nodes[idx][0] < query:
                _, r, c = nodes[idx]

                visited[r*COLS+c] = 1
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if 0<=row<ROWS and 0<=col<COLS and visited[row*COLS+col]: # only union visited node 
                        union(row*COLS+col, r*COLS+c)
                idx += 1

            if visited[0]:
                ans[idxQ] = rank[find(0)] # find current union size
        return ans