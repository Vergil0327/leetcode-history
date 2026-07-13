class Solution:
    def maxConsistentColumns(self, grid: list[list[int]], limit: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # 每一行自己單獨存在時，合法長度都是 1
        dp = [1] * n
        res = 1 # 既然 1 <= n，最少也能留下 1 行
        
        for j1 in range(n):
            for j2 in range(j1):
                # 優化：利用 Python 的 all() 進行短路求值 (Short-circuiting)
                # 只要有一列的差值大於 limit，all() 就會立刻中斷，比手寫 flag 快很多
                if all(abs(grid[r][j1] - grid[r][j2]) <= limit for r in range(m)):
                    dp[j1] = max(dp[j1], dp[j2] + 1)
                    
            if dp[j1] > res:
                res = dp[j1]
                
        return res