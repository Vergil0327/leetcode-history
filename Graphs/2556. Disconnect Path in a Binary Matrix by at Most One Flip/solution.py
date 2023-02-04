# DFS
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r >= m or c >= n or grid[r][c] == 0: return False
            if r == m-1 and c == n-1: return True
            
            if (r,c) != (0,0):
                grid[r][c] = 0

            if r+1 < m:
                if dfs(r+1, c): return True
            if c+1 < n:
                if dfs(r, c+1): return True
            return False

        if not dfs(0, 0): return True
        return not dfs(0, 0)

# BFS
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        queue = deque([(0,0)])
        visited = set()
        canBlock = False
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r+1 < m and grid[r+1][c] and (r+1, c) not in visited:
                    if r == m-1 and c == n-1:
                        break
                    visited.add((r+1, c))
                    queue.append((r+1, c))
                if c+1 < n and grid[r][c+1] and (r, c+1) not in visited:
                    if r == m-1 and c == n-1:
                        break
                    queue.append((r, c+1))
                    visited.add((r, c+1))
            if len(queue) < 2:
                canBlock = True if not queue or (queue[0] != (0,0) and queue[0] != (m-1, n-1)) else False
                break
        return canBlock
