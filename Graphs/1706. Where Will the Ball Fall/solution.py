# time complexity: O(ROWS * COLS)

class DFSSolution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(row, col):
            if not (col >= 0 and col < COLS):
                return -1

            if row == ROWS: return col
            
            if grid[row][col] == 1 and col+1<COLS and grid[row][col+1] != -1:
                return dfs(row+1, col+1)
            elif grid[row][col] == -1 and col > 0 and grid[row][col-1] != 1:
                return dfs(row+1, col-1)
            else:
                return -1
        
        res = [-1] * COLS
        for c in range(COLS):
            idx = dfs(0, c)
            if idx != -1:
                res[c] = idx

        return res

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = [-1] * COLS
        
        for col in range(COLS):
            row = 0
            ball = col
            while row < ROWS:
                if not (ball >=0 and ball < COLS):
                    break
                
                if grid[row][ball] == 1 and ball+1<COLS and grid[row][ball+1] != -1:
                    row += 1
                    ball += 1
                elif grid[row][ball] == -1 and ball > 0 and grid[row][ball-1] != 1:
                    row += 1
                    ball -= 1
                else:
                    break
                    
            if row == ROWS:
                res[col] = ball

        return res