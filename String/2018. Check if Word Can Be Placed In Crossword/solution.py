class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        t = len(word)
        revWord = word[::-1]

        def check(s):
            valid = validRev = True
            for k in range(t):
                if s[k] == " ": continue
                if s[k] != word[k]:
                    valid = False
                if s[k] != revWord[k]:
                    validRev = False

            return valid or validRev

        for i in range(m):
            j = 0
            while j < n:
                if board[i][j] == "#":
                    j += 1
                    continue
                
                jj = j
                s = ""
                while jj < n and board[i][jj] != "#":
                    s += board[i][jj]
                    jj += 1

                if len(s) == t:
                    if check(s): return True
                    
                j = jj
                j += 1

        for j in range(n):
            i = 0
            while i < m:
                if board[i][j] == "#":
                    i += 1
                    continue

                ii = i
                s = ""
                while ii < m and board[ii][j] != "#":
                    s += board[ii][j]
                    ii += 1

                if len(s) == t:
                    if check(s): return True
                    
                i = ii
                i += 1

        return False
