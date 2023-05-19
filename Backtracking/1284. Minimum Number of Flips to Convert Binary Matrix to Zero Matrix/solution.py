class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        original = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                original[r][c] = mat[r][c]

        def check(mat):
            for r in range(m):
                for c in range(n):
                    if mat[r][c] == 1: return False
            return True

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        def flips(r, c):
            mat[r][c] = 1-mat[r][c]
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0 <= row < m and 0 <= col < n:
                    mat[row][col] = 1-mat[row][col]

        def backtracking(r, c):
            if c == n:
                return backtracking(r+1, 0)
            if r == m:
                return 0 if check(mat) else inf

            res = backtracking(r, c+1)

            flips(r, c)
            res = min(res, backtracking(r, c+1)+1)
            flips(r, c)

            return res

        if (res := backtracking(0, 0)) == inf:
            return -1
        else:
            return res