from collections import deque
class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0]*m for _ in range(n)]

        seen = set()
        queue = deque()
        for r, c, color in sources:
            queue.append([r, c, color])
            seen.add((r,c))
            grid[r][c] = color
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            processed = {}
            for _ in range(len(queue)):
                r, c, color = queue.popleft()
                grid[r][c] = color

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= n or col < 0 or col >=m: continue
                    pos = (row, col)
                    if pos in seen: continue
                    processed[pos] = max(processed.get(pos, 0), color)
                    
            # use `processed` map to remove duplicate (avoid MLE !!!)
            # add to `seen` set to avoid TLE
            for r, c in processed:
                queue.append((r, c, processed[r,c]))
                seen.add((r,c))
        return grid