class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        left = [[0] * n for _ in range(m)]
        for i in range(m):
            cnt = 0
            for j in range(n):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                left[i][j] = cnt
        
        right = [[0] * n for _ in range(m)]
        for i in range(m):
            cnt = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    cnt = 0
                else:
                    cnt += 1
                right[i][j] = cnt

        # dp[i][j]: the maximum radius of pyramid when apex is grid[i][j]
        dp = [[0]*n for _ in range(m)]
        dpInv = [[0]*n for _ in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue

                # pyrimidal
                if i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(min(left[i][j], right[i][j]), dp[i-1][j]+1)
                res += dp[i][j]-1

        for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 0: continue

                if i == m-1:
                    dpInv[i][j] = 1
                else:                   
                    dpInv[i][j] = min(min(left[i][j], right[i][j]), dpInv[i+1][j]+1)
                res += dpInv[i][j]-1

        return res