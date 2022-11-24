class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        # i: keep tracking current word[i]
        def dfs(i, r, c, visited):
            if i == len(word)-1: return True

            for dr, dc in dirs:
                row, col = r+dr, c+dc

                if 0 <= row < ROWS and 0 <= col < COLS and (row,col) not in visited:
                    visited.add((row, col))

                    if board[row][col] == word[i+1]: 
                        if dfs(i+1, row, col, visited): return True
                    visited.remove((row, col))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c, set([(r,c)])): return True
        return False

class TrieNode:
    def __init__(self):
        self.next = {}
        self.end = False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        root = TrieNode()
        curr = root
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode()
            curr = curr.next[c]
        curr.end = True

        def dfs(r, c, root, visited):
            if (r,c) in visited: return False
            visited.add((r, c))
            
            # must check if we visited it before we check if we found the word
            if root.end: return True

            for dr, dc in dirs:
                row, col = r+dr, c+dc

                if 0 <= row < ROWS and 0 <= col < COLS:
                    ch = board[row][col]
                    if ch in root.next:
                        if dfs(row, col, root.next[ch], visited): return True
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.next:
                    if dfs(r, c, root.next[board[r][c]], set()): return True
        return False