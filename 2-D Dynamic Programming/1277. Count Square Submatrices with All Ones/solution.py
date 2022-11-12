class SolutionTopDown:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        memo = {}
        def dfs(r, c):
            if r == m or c == n: return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            if matrix[r][c] == 1:
                memo[(r,c)] = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))
            else:
                memo[(r,c)] = 0
            return memo[(r,c)]
        
        cnt = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]:
                    cnt += dfs(row, col)

        return cnt

class SolutionBottomUp:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = matrix[i-1][j-1]

        total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    total +=  dp[i][j]

        # return sum(map(sum, dp))
        return total

class SolutionSpaceOptimized:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        dp, prevDp = [0]*(n+1), [0]*(n+1)

        total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[j] = matrix[i-1][j-1] # initialization

                if matrix[i-1][j-1] == 1:
                    dp[j] = 1 + min(prevDp[j-1], prevDp[j], dp[j-1])
                    total += dp[j]
            dp, prevDp = prevDp, dp

        return total