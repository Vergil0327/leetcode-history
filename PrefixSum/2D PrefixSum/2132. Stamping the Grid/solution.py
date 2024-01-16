class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # find valid bottom-right position for stamps
        presum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] - presum[i][j] + (1-grid[i][j])

        stamp = [[0]*n for _ in range(m)]
        for i in range(stampHeight, m+1):
            for j in range(stampWidth, n+1):
                area = presum[i][j] - presum[i][j-stampWidth] - presum[i-stampHeight][j] + presum[i-stampHeight][j-stampWidth]
                
                if area != stampHeight * stampWidth: continue
                # we can stamp on grid[i][j] as bottom-right position of stamp
                stamp[i-1][j-1] += 1

        # check how many valid stamps
        stampPresum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                stampPresum[i+1][j+1] = stampPresum[i+1][j] + stampPresum[i][j+1] - stampPresum[i][j] + stamp[i][j]

        # check if we can cover every grid[i][j] where grid[i][j] == 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    row, col = min(i+stampHeight, m), min(j+stampWidth, n)
                    numStamp = stampPresum[row][col] - stampPresum[i][col] - stampPresum[row][j] + stampPresum[i][j]
                    if numStamp == 0: return False
        return True
