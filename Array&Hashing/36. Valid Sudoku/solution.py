class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rowM = defaultdict(set)
        colM = defaultdict(set)
        squareM = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".": continue
                s = board[r][c]
                if s in rowM[r]: return False
                if s in colM[c]: return False
                if s in squareM[(r//3, c//3)]: return False
                rowM[r].add(s)
                colM[c].add(s)
                squareM[(r//3, c//3)].add(s)
        return True

# https://leetcode.com/problems/valid-sudoku/discuss/15472/Short%2BSimple-Java-using-Strings
# One Hashmap Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = defaultdict(bool)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".": continue
                key = f"({board[r][c]})"
                if visited[f"{r}{key}"]: return False
                if visited[f"{key}{c}"]: return False
                if visited[f"{r//3}{key}{c//3}"]: return False
                visited[f"{r}{key}"] = True
                visited[f"{key}{c}"] = True
                visited[f"{r//3}{key}{c//3}"] = True
        return True
