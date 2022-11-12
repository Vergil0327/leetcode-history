# https://leetcode.com/problems/maximal-square/discuss/61803/C%2B%2B-space-optimized-DP
# https://www.youtube.com/watch?v=eg6g6cNvsTs

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: the side length of largest square containing only 1's
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
        # base case
        for r in range(1, ROWS+1):
            for c in range(1, COLS+1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = 1

        for i in range (1, ROWS+1):
            for j in range(1, COLS+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        return max(map(max, dp)) ** 2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j]: the side length of largest square containing only 1's
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # initialization
        dp = [0]*(COLS+1)
        prevDp = [0]*(COLS+1)

        maxSideLen = 0
        for i in range (1, ROWS+1):
            # base case
            for j in range(1, COLS+1):
                dp[j] = ord(matrix[i-1][j-1]) - ord("0")
            for j in range(1, COLS+1):
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(prevDp[j-1], prevDp[j], dp[j-1])+1
                    maxSideLen = max(maxSideLen, dp[j])
            dp, prevDp = prevDp, dp
        
        return maxSideLen ** 2

class SolutionTopDown:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        @functools.lru_cache(None)
        def dfs(r, c):
            if r == ROWS or c == COLS:
                return 0
            
            sideLen = 0
            if matrix[r][c] == "1":
                sideLen = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
                
            return sideLen

        maxSideLen = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxSideLen = max(maxSideLen, dfs(r, c))
        return maxSideLen ** 2