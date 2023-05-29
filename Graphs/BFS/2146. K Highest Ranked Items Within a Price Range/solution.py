class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        WALL = 0

        m, n = len(grid), len(grid[0])

        queue = deque([(start[0], start[1], 0)])
        topK = []
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                r, c, dist = queue.popleft()
                if grid[r][c] == WALL: continue

                if pricing[0] <= grid[r][c] <= pricing[1]:
                    topK.append((dist, grid[r][c], r, c))
                
                grid[r][c] = WALL # mark visited

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if 0 <= row < m and 0 <= col < n:
                        if grid[row][col] == WALL: continue
                        queue.append((row, col, dist+1))
        topK.sort()
        res = []
        for i in range(min(k, len(topK))):
            _, _, row, col = topK[i]
            res.append([row, col])
        return res
