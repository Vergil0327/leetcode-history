class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        
        row1sum = [0] * ROWS
        col1sum = [0] * COLS
        row0sum = [0] * ROWS
        col0sum = [0] * COLS
        
        for r in range(ROWS):
            for c in range(COLS):
                row1sum[r] += grid[r][c]
                col1sum[c] += grid[r][c]
                if grid[r][c] == 0:
                    row0sum[r] += 1
                    col0sum[c] += 1
                    
        diff = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                diff[r][c] = row1sum[r]+col1sum[c]-row0sum[r]-col0sum[c]
        return diff

# optimized, we can use just two array
# num = 1: +1
# num = 0: -1
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        
        def calculate(nums):
            total = 0
            for num in nums:
                if num == 1:
                    total += 1
                else:
                    total -= 1
            return total

        rowsum = [calculate(row) for row in grid]
        colsum = [calculate(col) for col in zip(*grid)] # zip(*grid) will transpose gird, which means zip(grid[0], grid[1], grid[2], ...)
    
        diff = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                diff[r][c] = rowsum[r]+colsum[c]
        return diff