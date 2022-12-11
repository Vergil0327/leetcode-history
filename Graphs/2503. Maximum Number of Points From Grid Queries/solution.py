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