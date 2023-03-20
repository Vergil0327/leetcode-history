class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        @lru_cache(None)
        def dfs(r, c):
            if r >= n: return 0
            if c < 0 or c >= n: return inf

            res = inf
            for col in range(-1, n+1):
                if col != c:
                    res = min(res, dfs(r+1, col))
            return res + grid[r][c]
        
        return min(dfs(0, i) for i in range(n))

# bottom-up
class Solution_TLE:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[inf] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(n):
                for prev in range(n):
                    if prev == j: continue
                    dp[i][j] = min(dp[i][j], dp[i-1][prev] + grid[i][j])

        return min(dp[n-1])
    
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            prevMin = []
            for prev in range(n):
                prevMin.append([dp[i-1][prev], prev])
            prevMin.sort()
            
            for j in range(n):
                if prevMin[0][1] != j:
                    dp[i][j] = prevMin[0][0] + grid[i][j]
                elif len(prevMin) > 1 and prevMin[1][1] != j:
                    dp[i][j] = prevMin[1][0] + grid[i][j]
                
        return min(dp[n-1])