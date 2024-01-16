# BFS
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        if m==1 and n==1: return grid[0][0] == 0

        queue = deque([(m-1, n-1)])
        seen = [[0]*n for _ in range(m)]
        seen[m-1][n-1] = 1

        dirs = [[-1, 0], [0, -1]]
        canReach = False
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == 0 and c == 0:
                    canReach = True
                    break

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or col < 0: continue
                    if grid[row][col] == 0: continue
                    if seen[row][col]: continue
                    seen[row][col] = 1
                    queue.append((row, col))

        if not canReach: return True

        queue = deque([(0,0)])
        visited = [[0]*n for _ in range(m)]

        dirs = [[1, 0], [0, 1]]
        canBlock = False
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == m-1 and c == n-1: break

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row >=m or col >= n: continue

                    if not seen[row][col]: continue # the path which can't reach destination

                    if visited[row][col]: continue
                    visited[row][col] = 1

                    queue.append((row, col))
            
            if len(queue) < 2:
                canBlock = not queue or queue[0] not in {(0,0), (m-1, n-1)}
                break

        return canBlock
