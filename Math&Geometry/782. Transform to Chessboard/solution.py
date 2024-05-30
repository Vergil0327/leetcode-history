class Solution:
    def checkPossible(self, board):
        n = len(board)

        # check rows
        typ1 = typ2 = 0
        typ1 += 1 # choose row1 as typ1
        for i in range(1, n):
            if board[i][0] == board[0][0]:
                typ1 += 1
                for j in range(n):
                    if board[i][j] != board[0][j]: return False
            else:
                typ2 += 1
                for j in range(n):
                    if board[i][j] == board[0][j]: return False
        
        if abs(typ1-typ2) > 1: return False # typ1, typ2應該為n//2 或 {n//2, (n+1)//2}

        # check columns
        typ1 = typ2 = 0
        typ1 += 1 # column1 as typ1
        for j in range(1, n):
            if board[0][j] == board[0][0]:
                typ1 += 1
                for i in range(n):
                    if board[i][0] != board[i][j]: return False
            else:
                typ2 += 1
                for i in range(n):
                    if board[i][0] == board[i][j]: return False
        if abs(typ1-typ2) > 1: return False # typ1, typ2應該為n//2 或 {n//2, (n+1)//2}
        return True

    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        if not self.checkPossible(board): return -1

        res = diffRow = diffCol = 0
        for j in range(n):
            diffRow += int(board[0][j] != j%2)
            # diffRowTyp2 += (board[0][j] == i%2) => 實際上就是n-diffRow
        for i in range(n):
            diffCol += int(board[i][0] != i%2)

        if n%2 == 0:
            res += min(diffRow, n-diffRow)
            res += min(diffCol, n-diffCol)
        else:
            # 11100 -> 10101
            res += diffRow if diffRow%2 == 0 else n-diffRow
            res += diffCol if diffCol%2 == 0 else n-diffCol

        return res//2
