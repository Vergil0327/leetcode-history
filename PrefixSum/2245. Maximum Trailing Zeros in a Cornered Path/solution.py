class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                cnt2, cnt5 = 0, 0
                while grid[r][c]%5 == 0:
                    grid[r][c] //= 5
                    cnt5 += 1
                while grid[r][c]%2 == 0:
                    grid[r][c] //= 2
                    cnt2 += 1
                grid[r][c] = [cnt2, cnt5] # each cell: [# of 2, # of 5]
        
        presumRow = [[[0,0] for _ in range(COLS)] for _ in range(ROWS+1)]
        for r in range(1, ROWS+1):
            for c in range(COLS):
                presumRow[r][c][0] = presumRow[r-1][c][0] + grid[r-1][c][0]
                presumRow[r][c][1] = presumRow[r-1][c][1] + grid[r-1][c][1]
        
        presumCol = [[[0,0] for _ in range(COLS+1)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(1, COLS+1):
                presumCol[r][c][0] = presumCol[r][c-1][0] + grid[r][c-1][0]
                presumCol[r][c][1] = presumCol[r][c-1][1] + grid[r][c-1][1]

        zeros = 0
        for r in range(ROWS):
            for c in range(COLS):
                cnt2FromTop, cnt5FromTop = presumRow[r+1][c]
                cnt2FromBot, cnt5FromBot = presumRow[ROWS][c][0] - presumRow[r][c][0], presumRow[ROWS][c][1] - presumRow[r][c][1]
                
                leftFromTop = min(
                    cnt2FromTop+presumCol[r][c+1][0]-grid[r][c][0],
                    cnt5FromTop+presumCol[r][c+1][1]-grid[r][c][1],
                )
                leftFromBot = min(
                    cnt2FromBot+presumCol[r][c+1][0]-grid[r][c][0],
                    cnt5FromBot+presumCol[r][c+1][1]-grid[r][c][1],
                )
                rightFromTop = min(
                    cnt2FromTop+presumCol[r][COLS][0]-presumCol[r][c][0]-grid[r][c][0],
                    cnt5FromTop+presumCol[r][COLS][1]-presumCol[r][c][1]-grid[r][c][1],
                )
                rightFromBot = min(
                    cnt2FromBot+presumCol[r][COLS][0]-presumCol[r][c][0]-grid[r][c][0],
                    cnt5FromBot+presumCol[r][COLS][1]-presumCol[r][c][1]-grid[r][c][1],
                )
                zeros = max(zeros, leftFromTop, leftFromBot,rightFromTop,rightFromBot)
        return zeros