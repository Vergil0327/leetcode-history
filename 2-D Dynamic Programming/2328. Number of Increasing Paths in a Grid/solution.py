class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[1] * n for _ in range(m)]

        minHeap = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(minHeap, [grid[i][j], i, j])

        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        while minHeap:
            v, x, y = heapq.heappop(minHeap)
            for dx, dy in dirs:
                xx, yy = x+dx, y+dy
                if 0 <= xx < m and 0 <= yy < n:
                    if grid[xx][yy] > v:
                        dp[xx][yy] += dp[x][y]
        mod = 10**9 + 7
        res = 0
        for i in range(m):
            for j in range(n):
                res = (res + dp[i][j])%mod
        return res


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        
        dp = [[-1]*n for _ in range(m)]
        def dfs(r, c):
            if dp[r][c] != -1: return dp[r][c]

            res = 1
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0<=row<m and 0<=col<n and grid[row][col] > grid[r][c]:
                    res += dfs(row, col)

            dp[r][c] = res
            return res

        res = 0
        for r in range(m):
            for c in range(n):
                res += dfs(r, c)
                res %= mod
        return res