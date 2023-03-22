class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        cache = [[[-1] * k for _ in range(n)] for _ in range(m)]
        def dfs(i, j, total):
            if i >= m or j >= n: return 0
            if i == m-1 and j == n-1:
                return 1 if (total+grid[i][j])%k == 0 else 0
            if cache[i][j][total] != -1: return cache[i][j][total]

            cache[i][j][total] = dfs(i+1, j, (total + grid[i][j])%k) + dfs(i, j+1, (total + grid[i][j])%k)
            cache[i][j][total] %= 1_000_000_007
            return cache[i][j][total]
        return dfs(0, 0, 0)

class Solution_TLE:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j, total):
            if i >= m or j >= n: return 0
            if i == m-1 and j == n-1:
                return 1 if (total+grid[i][j])%k == 0 else 0

            res = dfs(i+1, j, (total + grid[i][j])%k)
            res %= 1_000_000_007
            res += dfs(i, j+1, (total + grid[i][j])%k)
            res %= 1_000_000_007
            return res
        return dfs(0, 0, 0)