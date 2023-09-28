class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        pq = [[0, 0, 0]] # [remove, row, col]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while pq:
            rm, r, c = heapq.heappop(pq)
            if r == m-1 and c == n-1: return rm
            if grid[r][c] == -1: continue
            grid[r][c] = -1

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if grid[row][col] == -1: continue
                heapq.heappush(pq, [rm + grid[row][col], row, col])
                        
        return 0