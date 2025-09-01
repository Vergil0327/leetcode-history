MIRROW = 1
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dirs = [(0,1), (1,0)]

        @cache
        def dfs(r, c, d):
            if r == m-1 and c == n-1: return 1
            if r < 0 or r >= m or c < 0 or c >= n: return 0

            res = 0
            if grid[r][c] == MIRROW:
                d = 1-d
                dr, dc = dirs[d]
                row, col = r+dr, c+dc
                res += dfs(row, col, d)
            else:
                for i, (dr, dc) in enumerate(dirs):
                    row, col = r+dr, c+dc
                    res += dfs(row, col, i)
            
            return res % mod

        return dfs(0, 0, -1)