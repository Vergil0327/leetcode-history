# 2023/09/14 daily challenge
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t = grid[0][0]

        pq = [[0,0,0]]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = [[0]*n for _ in range(n)]
        while True:
            while pq and pq[0][0] <= t:
                _, r, c = heapq.heappop(pq)
                if r == n-1 and c==n-1: return t
                if visited[r][c]: continue
                visited[r][c] = 1

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row>=n or col<0 or col>=n: continue
                    heapq.heappush(pq, [grid[row][col], row, col])

            t += 1
    
