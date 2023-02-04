class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n or grid[r][c] == 0: return False
            if r == m-1 and c == n-1: return True
            
            if (r,c) != (0,0):
                grid[r][c] = 0

            if r+1 < m:
                if dfs(r+1, c): return True
            if c+1 < n:
                if dfs(r, c+1): return True
            return False

        if not dfs(0, 0): return True
        return not dfs(0, 0)
