class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]

        def dfs(r, c):
            if dp[r][c] != -1: return dp[r][c]
            num = grid[r][c]
            col = c+1
            
            res = 0
            if col < n:
                if r-1 >= 0 and grid[r-1][col] > num:
                    res = max(res, dfs(r-1, col)+1)

                if grid[r][col] > num:
                    res = max(res, dfs(r, col)+1)

                if r+1<m and grid[r+1][col] > num:
                    res = max(res, dfs(r+1, col)+1)

            dp[r][c] = res
            return dp[r][c]
        
        res = 0
        for row in range(m):
            res = max(res, dfs(row, 0))
        return res
        