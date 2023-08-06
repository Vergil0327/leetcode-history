# TLE Brute Force
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        thief = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    thief.add((i, j))
        if (0,0) in thief or (m-1, n-1) in thief: return 0
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c, visited):
            if r == m-1 and c == n-1: return True
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if (row, col) in thief: continue
                if (row, col) in visited: continue
                visited.add((row, col))
                if dfs(row, col, visited): return True
            return False
            
        res = 0
        while dfs(0, 0, set([(0,0)])):
            if (0,0) in thief or (m-1, n-1) in thief: return res
            nxt = thief.copy()
            for r,c in thief:
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    nxt.add(((row, col)))
            thief = nxt
            
            res += 1
        return res