class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # dp[i][j][x][y]: the maximum number of cherries we can pick up at (i, j) and (x, y)
        dp = [[[-inf] * (n+1) for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                for x in range(1, n+1):
                    y = i+j-x
                    if y < 0 or y >n: continue
                    if grid[i-1][j-1] == -1 or grid[x-1][y-1] == -1: continue

                    if i == 1 and j == 1 and x == 1 and y == 1:
                        dp[i][j][x] = grid[i-1][j-1]
                        continue
                    
                    dp[i][j][x] = max(dp[i][j][x], dp[i-1][j][x-1])
                    dp[i][j][x] = max(dp[i][j][x], dp[i][j-1][x-1])
                    dp[i][j][x] = max(dp[i][j][x], dp[i][j-1][x])
                    dp[i][j][x] = max(dp[i][j][x], dp[i-1][j][x])
                    if (i, j) != (x, y):
                        dp[i][j][x] += grid[i-1][j-1] + grid[x-1][y-1]
                    else:
                        dp[i][j][x] += grid[i-1][j-1]
        return dp[n][n][n] if dp[n][n][n] != -inf else 0

class Solution_TLE:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # dp[i][j][x][y]: the maximum number of cherries we can pick up at (i, j) and (x, y)
        dp = [[[[-inf] * (n+1) for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                for x in range(1, n+1):
                    y = i+j-x
                    if y < 0 or y >n: continue
                    if grid[i-1][j-1] == -1 or grid[x-1][y-1] == -1: continue

                    if i == 1 and j == 1 and x == 1 and y == 1:
                        dp[i][j][x][y] = grid[i-1][j-1]
                        continue
                    
                    dp[i][j][x][y] = max(dp[i][j][x][y], dp[i-1][j][x-1][y])
                    dp[i][j][x][y] = max(dp[i][j][x][y], dp[i][j-1][x-1][y])
                    dp[i][j][x][y] = max(dp[i][j][x][y], dp[i][j-1][x][y-1])
                    dp[i][j][x][y] = max(dp[i][j][x][y], dp[i-1][j][x][y-1])
                    if (i, j) != (x, y):
                        dp[i][j][x][y] += grid[i-1][j-1] + grid[x-1][y-1]
                    else:
                        dp[i][j][x][y] += grid[i-1][j-1]
        return dp[n][n][n][n] if dp[n][n][n][n] != -inf else 0
