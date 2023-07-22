# top-down
class Solution:
    def knightProbability(self, n: int, K: int, ROW: int, COLUMN: int) -> float:
        dirs = [[1, 2], [1, -2],[-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

        memo = [[[-1]*(K+1) for _ in range(n)] for _ in range(n)]

        def dfs(r, c, k):
            if k == 0: return 1
            if memo[r][c][k] != -1: return memo[r][c][k]

            res = 0
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= n or col < 0 or col >= n:
                    continue
                res += dfs(row, col, k-1) * 1/8
            
            memo[r][c][k] = res
            return memo[r][c][k]
        return dfs(ROW, COLUMN, K)

# bottom-up
class Solution:
    def knightProbability(self, n: int, K: int, ROW: int, COLUMN: int) -> float:
        dirs = [[1, 2], [1, -2],[-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

        dp = [[[0]*(K+1) for _ in range(n)] for _ in range(n)]
        dp[ROW][COLUMN][K] = 1
        while K:
            for r in range(n):
                for c in range(n):
                    if dp[r][c][K] != 0:
                        for dr, dc in dirs:
                            row, col = r+dr, c+dc
                            if row < 0 or row >= n or col < 0 or col >= n:
                                continue
                            dp[row][col][K-1] += dp[r][c][K] * 1/8
            K -= 1
        
        prob = 0
        for r in range(n):
            for c in range(n):
                prob += dp[r][c][0]
        return prob

# bot-up BFS
class Solution:
    def knightProbability(self, n: int, K: int, ROW: int, COLUMN: int) -> float:
        dirs = [[1, 2], [1, -2],[-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

        dp = [[[0]*(K+1) for _ in range(n)] for _ in range(n)]
        dp[ROW][COLUMN][K] = 1
        queue = set([(ROW, COLUMN)])
        while K:
            nxtQueue = set() # next valid position
            for r, c in queue:
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= n or col < 0 or col >= n:
                        continue
                    dp[row][col][K-1] += dp[r][c][K] * 1/8
                    nxtQueue.add((row, col))
            K -= 1
            queue = nxtQueue
        
        prob = 0
        for r in range(n):
            for c in range(n):
                prob += dp[r][c][0]
        return prob
