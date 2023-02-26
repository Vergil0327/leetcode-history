class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # only edge case we can't reach destination
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        
        m, n = len(grid), len(grid[0])
        
        queue = [(0,0,0)] # current time, row, col
        visited = set([(0, 0)])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            
            time, r, c = heapq.heappop(queue)
        
            if r == m-1 and c == n-1:
                return time
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if (row, col) in visited: continue
                visited.add((row, col))
                if grid[row][col] <= time+1:
                    heapq.heappush(queue, (time+1, row, col))
                else:
                    backForth = grid[row][col] - time
                    if backForth%2 == 0:
                        backForth += 1
                    heapq.heappush(queue, (time+backForth, row, col))

        return -1


class Solution_TLE:
    def minimumTime(self, grid: List[List[int]]) -> int:
        time = 0
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)])

        visited = set([(0, 0)])
        DIRS = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m-1 and c == n-1: return time-1
                
                for dr, dc in DIRS:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] <= time:
                        visited.add((row, col))
                        queue.append((row, col))        
        return -1