# top-down DP
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = int(1e9+7)
        dirs = [[-1,0], [1,0], [0, 1], [0, -1]]

        @lru_cache(None)
        def dfs(r, c, move):
            if move > maxMove: return 0
            if r < 0 or r == m or c < 0 or c == n:
                if move <= maxMove:
                    return 1
                else:
                    return 0

            res = 0
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                res += dfs(row, col, move+1)
                res %= MOD
            return res
        return dfs(startRow, startColumn, 0)
    
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = int(1e9+7)
        dirs = [[-1,0], [1,0], [0, 1], [0, -1]]

        dp = [[[0]*(maxMove+1) for _ in range(n+2)] for _ in range(m+2)]
        for r in range(m+2):
            for move in range(maxMove+1):
                dp[r][0][move] = 1
                dp[r][n+1][move] = 1
        for c in range(n+1):
            for move in range(maxMove+1):
                dp[0][c][move] = 1
                dp[m+1][c][move] = 1
        
        for move in range(1, maxMove+1):
            for r in range(1, m+1):
                for c in range(1, n+1):
                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        dp[r][c][move] += dp[row][col][move-1]
                        dp[r][c][move] %= MOD
        return dp[startRow+1][startColumn+1][maxMove]