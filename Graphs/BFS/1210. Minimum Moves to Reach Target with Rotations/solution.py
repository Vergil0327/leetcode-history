class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:        
        m, n = len(grid), len(grid[0])
        if grid[m-1][n-2] == 1 or grid[m-1][n-1] == 1: return -1

        dirs = [[1,0],[0,1]] # only move right or move down
        queue = deque([((0,0),(0,1))])
        visited = set([((0,0),(0,1))])
        step = 0
        while queue:
            for _ in range(len(queue)):
                p1, p2 = queue.popleft()
                r1, c1 = p1
                r2, c2 = p2
                
                if r1 == m-1 and c1 == n-2 and r2 == m-1 and c2 == n-1: return step

                for dr, dc in dirs:
                    row1, col1 = r1+dr, c1+dc
                    row2, col2 = r2+dr, c2+dc
                    
                    if row1 < 0 or row1 >= m or col1 < 0 or col1 >= n: continue
                    if row2 < 0 or row2 >= m or col2 < 0 or col2 >= n: continue
                    if grid[row1][col1] or grid[row2][col2]: continue # wall
                    if ((row1, col1),(row2,col2)) in visited: continue
                    visited.add(((row1, col1),(row2,col2)))
                    queue.append(((row1, col1),(row2,col2)))

                # clockwise rotate if snake is horizontal
                if r1 == r2 and c1+1 == c2:
                    row1, col1 = r1, c1
                    row2, col2 = r2+1, c2-1
                    if (0 <= row2 < m and
                        0 <= col2 < n and
                        grid[row2][col2] == 0 and 
                        0 <= row1+1 < m and
                        0 <= col1+1 < n and
                        grid[row1+1][col1+1] == 0 and 
                        ((row1,col1),(row2,col2)) not in visited):
                        nxt = ((row1,col1),(row2,col2))
                        visited.add(nxt)
                        queue.append(nxt)

                # counter-clockwise rotate if snake if vertical
                if r1+1 == r2 and c1 == c2:
                    row1, col1 = r1, c1
                    row2, col2 = r2-1, c2+1
                    if (0 <= row2 < m and
                        0 <= col2 < n and
                        grid[row2][col2] == 0 and 
                        0 <= row1+1 < m and
                        0 <= col1+1 < n and
                        grid[row1+1][col1+1] == 0 and 
                        ((row1,col1),(row2,col2)) not in visited):
                        nxt = ((row1,col1),(row2,col2))
                        visited.add(nxt)
                        queue.append(nxt)
            step += 1
        return -1
