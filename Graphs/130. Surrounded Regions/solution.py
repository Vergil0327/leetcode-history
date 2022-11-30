class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r, c, visited):
            if (r,c) in visited: return
            visited.add((r,c))
            
            if board[r][c] == "O":
                board[r][c] = "#"
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0 <= row < m and 0<= col < n:
                    if board[row][col] == "O":
                        dfs(row, col, visited)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "X": continue
                if r == 0 or r == m-1:
                    dfs(r, c, set())
                if c == 0 or c == n-1:
                    dfs(r,c, set())

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"