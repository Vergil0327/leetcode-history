# Bottom-Up
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[inf] * (n+2) for _ in range(n+2)]
        for i in range(n+1):
            dp[0][i] = 0
        
        for r in range(1, n+1):
            for c in range(1, n+1):
                dp[r][c] = min(matrix[r-1][c-1] + dp[r-1][c-1], matrix[r-1][c-1]+dp[r-1][c], matrix[r-1][c-1]+dp[r-1][c+1])

        return min(dp[n])

# Space-Optimized Bottom-Up
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [inf] * (n+2)
        curr = [inf] * (n+2)

        # base case
        for i in range(1, n+1):
            prev[i] = 0
        
        for r in range(1, n+1):
            for c in range(1, n+1):
                # dp[r][c] = min(matrix[r-1][c-1] + dp[r-1][c-1], matrix[r-1][c-1]+dp[r-1][c], matrix[r-1][c-1]+dp[r-1][c+1])
                curr[c] = min(matrix[r-1][c-1]+prev[c-1], matrix[r-1][c-1]+prev[c], matrix[r-1][c-1]+prev[c+1])
            prev, curr = curr, prev

        return min(prev)

# Top-Down + Memorization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @functools.lru_cache(None)
        def dfs(row, col):
            if row == n: return 0
            if col < 0 or col >= n: return inf

            SUM = matrix[row][col]
            SUM += min(dfs(row+1, col-1), dfs(row+1, col), dfs(row+1, col+1))
            return SUM
        
        res = inf
        for c in range(n):
            res = min(res, dfs(0, c))
        return res
