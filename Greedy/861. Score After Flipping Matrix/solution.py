class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1-grid[i][j]
        
        cnt = [0] * n
        cnt[0] = m

        for j in range(1, n):
            for i in range(m):
                cnt[j] += grid[i][j]
            if cnt[j] < m/2:
                cnt[j] = m-cnt[j]

        res = base = 0
        for j in range(n-1, -1, -1):
            res += cnt[j] * 2**base
            base += 1
        return res
