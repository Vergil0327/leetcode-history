# DFS - recursively
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ")" or grid[m-1][n-1] == "(": return False

        @lru_cache(None)
        def dfs(i, j, balanced: int):
            if i >= m or j >= n: return False
            if balanced < 0: return False

            v = 1 if grid[i][j] == "(" else -1
            if i == m-1 and j == n-1:
                return balanced+v == 0

            if dfs(i+1, j, balanced+v): return True
            if dfs(i, j+1, balanced+v): return True

            return False

        return dfs(0, 0, 0)
    
# DFS iteratively
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ")" or grid[m-1][n-1] == "(": return False

        stack = [[0, 0, 1 if grid[0][0] == "(" else -1]]
        visited = set()
        while stack:
            r, c, balanced = stack.pop()
            if balanced < 0: continue
            if r == m-1 and c == n-1 and balanced == 0: return True
            if (r,c,balanced) in visited: continue
            visited.add((r,c,balanced))

            if r+1 < m:
                v = 1 if grid[r+1][c] == "(" else -1
                stack.append([r+1, c, balanced+v])
            if c+1 < n:
                v = 1 if grid[r][c+1] == "(" else -1
                stack.append([r, c+1, balanced+v])
        return False
    
# Bottom-up
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]

        # base case
        if grid[0][0] == '(':
            dp[0][0] = set([1])
        else:
            return False
        
        for i in range(m):
            for j in range(n):
                v = 1 if grid[i][j] == "(" else -1

                if i >= 1:
                    for balanced in dp[i-1][j]:
                        if balanced+v >= 0:
                            dp[i][j].add(balanced+v)
                if j >= 1:
                    for balanced in dp[i][j-1]:
                        if balanced+v >= 0:
                            dp[i][j].add(balanced+v)
        return 0 in dp[m-1][n-1]