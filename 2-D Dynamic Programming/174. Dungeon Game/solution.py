class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        dp = [[float("inf")] * (COLS+1) for _ in range(ROWS+1)]
        
        
        # dp[i][j]: the knight's minimum initial health at (i, j) position
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if i == ROWS-1 and j == COLS-1: # base case
                    dp[ROWS-1][COLS-1] = -dungeon[ROWS-1][COLS-1]+1 if dungeon[ROWS-1][COLS-1] <= 0 else 1
                else:
                    minHealth = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                    dp[i][j] = minHealth if minHealth > 0 else 1
        return dp[0][0]

# since our dp only depends on next row, we can reduce 2-D array to 1-D array
class SpaceOptimizedSolution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        # dp = [[float("inf")] * (COLS+1) for _ in range(ROWS+1)]
        dp = [float("inf")] * (COLS+1)
        nextDp = [float("inf")] * (COLS+1)
        
        # dp[i][j]: the knight's minimum initial health at (i, j) position
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if i == ROWS-1 and j == COLS-1: # base case
                    dp[COLS-1] = -dungeon[ROWS-1][COLS-1]+1 if dungeon[ROWS-1][COLS-1] <= 0 else 1
                else:
                    minHealth = min(nextDp[j], dp[j+1]) - dungeon[i][j]
                    dp[j] = minHealth if minHealth > 0 else 1
            dp, nextDp = nextDp, dp

        return nextDp[0]

# https://labuladong.github.io/algo/3/28/87/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        @functools.lru_cache(None)
        def dfs(row, col):
            if row== ROWS-1 and col== COLS-1:
                return -dungeon[row][col]+1 if dungeon[row][col] <= 0 else 1
            
            # since we'll use min() to choose minimum health, use inf for out-of-bound condition
            if row >= ROWS or col >= COLS: return float("inf")
            
            minHealthForNext = min(dfs(row+1, col), dfs(row, col+1))
            minHealth = minHealthForNext - dungeon[row][col] # min required health at current (row, col)
            
            # 1 is minimum required health
            return minHealth if minHealth > 0 else 1
            
        return dfs(0, 0)

# https://www.youtube.com/watch?v=tUGfSr1V04I
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        
        # dp[i][j]: the knight's minimum initial health at dungeon[i][j] after increasing or decreasing health at dungeon[i][j]
        dp = [[1] *(COLS) for _ in range(ROWS)]
        
        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if i == ROWS-1 and j == COLS-1:
                    dp[i][j] = 1 # minimum initial health after taking item at [i,j]
                elif i == ROWS-1:
                    dp[i][j] = dp[i][j+1] - dungeon[i][j+1]
                elif j == COLS-1:
                    dp[i][j] = dp[i+1][j] - dungeon[i+1][j]
                else:
                    dp[i][j] = min(dp[i+1][j] - dungeon[i+1][j], dp[i][j+1] - dungeon[i][j+1])
                dp[i][j] = max(1, dp[i][j]) # minimum initial health can't be 0 or negative

        dp[0][0] = dp[0][0] - dungeon[0][0]
        dp[0][0] = max(1, dp[0][0])
        return dp[0][0]