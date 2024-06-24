class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        presum = [[0]*(n+1) for _ in range(m+1)]

        total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                total += grid[i-1][j-1]
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + grid[i-1][j-1]
        
        start = end = -1
        for i in range(1, m+1):
            if presum[i][n] != 0 and start == -1:
                start = i

            if presum[i][n] == total and end == -1:
                end = i
        height = end-start+1

        start = end = -1
        for j in range(1, n+1):
            if presum[m][j] != 0 and start == -1:
                start = j
            if presum[m][j] == total and end == -1:
                end = j
        width = end-start+1

        return width * height


                