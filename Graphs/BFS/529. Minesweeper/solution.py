class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        revealed = set()
        
        r,c = click
        revealed.add((r,c))
        
        neighbors = []
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        
        mines = 0
        for dr, dc in dirs:
            row, col = r+dr, c+dc
            if 0 <= row < m and 0 <= col < n:
                if board[row][col] == "M":
                    mines += 1
                else:
                    neighbors.append((row, col))

        board[r][c] = str(mines) if mines > 0 else "B"

        if board[r][c] == "B":
            queue = deque(neighbors)
            while queue:
                r, c = queue.popleft()
                if (r,c) in revealed: continue
                revealed.add((r,c))

                mines = 0
                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if 0 <= row < m and 0 <= col < n:
                        if board[row][col] in {"M", "X"}:
                            mines += 1
                if mines > 0:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = "B"
                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if 0 <= row < m and 0 <= col < n and board[row][col] == "E":
                            queue.append((row, col))

        return board