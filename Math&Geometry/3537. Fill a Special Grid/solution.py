class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        m = pow(2, N)
        self.grid = [[0]*(m) for _ in range(m)]
        self.val = 0

        def dfs(row_start, row_end, col_start, col_end):
            size = row_end-row_start
            if size == 1:
                self.grid[row_start][col_start] = self.val
                self.val += 1
                return
            half = size//2

            top_right = dfs(row_start, row_start+half, col_start+half, col_end)
            bottom_right = dfs(row_start+half, row_end, col_start+half, col_end)
            bottom_left = dfs(row_start+half, row_end, col_start, col_start+half)
            top_left = dfs(row_start, row_start+half, col_start, col_start+half)
            
        dfs(0, m, 0, m)
        return self.grid