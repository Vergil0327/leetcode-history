class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if k >= (m-1) + (n-1): return (m-1) + (n-1)
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        queue = deque([[0,0,k]])
        visited = [[[0]*(k+1) for _ in range(n)] for _ in range(m)]
        step = 0
        while queue:
            for _ in range(len(queue)):
                r, c, t = queue.popleft()
                if r == m-1 and c == n-1: return step
                if visited[r][c][t]: continue
                visited[r][c][t] = 1

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] == 1 and t > 0:
                        queue.append((row, col, t-1))
                    elif grid[row][col] == 0:
                        queue.append((row, col, t))
            step += 1

        return -1
