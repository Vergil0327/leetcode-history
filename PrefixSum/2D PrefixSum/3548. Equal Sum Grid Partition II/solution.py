class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        presum = [[0]*(n+1) for _ in range(m+1)]
        total = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                total += grid[i-1][j-1]
                presum[i][j] = presum[i-1][j] + presum[i][j-1] + grid[i-1][j-1] - presum[i-1][j-1]

        for i in range(1, m):
            top, bot = presum[i][n], total-presum[i][n]
            if top == bot: return True
            if top < bot:
                need = bot-top
                if need in {grid[i][0], grid[i][-1], grid[-1][0], grid[-1][-1]}: return True

            if top > bot:
                need = top-bot
                if need in {grid[i-1][0], grid[i-1][-1], grid[0][0], grid[0][-1]}: return True

        for j in range(1, n):
            left, right = presum[m][j], total-presum[m][j]
            if left == right: return True
            if left < right:
                need = right-left
                if need in {grid[0][j], grid[0][-1], grid[m-1][j], grid[m-1][-1]}: return True
            if left > right:
                need = left-right
                if need in {grid[0][0], grid[0][j-1], grid[m-1][0], grid[m-1][j-1]}: return True
        return False