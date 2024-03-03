class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        presum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                presum[i+1][j+1] = presum[i][j+1] + presum[i+1][j] + grid[i][j] - presum[i][j]
        
        res = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if presum[i][j] <= k: res += 1
        return res