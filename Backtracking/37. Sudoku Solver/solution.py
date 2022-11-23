class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        rowM = defaultdict(set)
        colM = defaultdict(set)
        squareM = defaultdict(set)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".": continue
                val = int(board[r][c])
                rowM[r].add(val)
                colM[c].add(val)
                squareM[(r//3, c//3)].add(val)
        
        def dfs(row, col):
            if col == COLS:
                return dfs(row+1, 0)
            if row == ROWS:
                return True
            if board[row][col] != ".":
                return dfs(row, col+1)


            for v in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if v in rowM[row]: continue
                if v in colM[col]: continue
                if v in squareM[(row//3, col//3)]: continue

                rowM[row].add(v)
                colM[col].add(v)
                squareM[(row//3, col//3)].add(v)
                board[row][col] = str(v)
                if dfs(row, col+1): return True
                board[row][col] = "."
                rowM[row].remove(v)
                colM[col].remove(v)
                squareM[(row//3, col//3)].remove(v)
            
            return False
        dfs(0, 0)