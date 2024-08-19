class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        best3 = [[(-inf, -1)]*3 for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] > best3[i][0][0]:
                    best3[i][2] = best3[i][1]
                    best3[i][1] = best3[i][0]
                    best3[i][0] = (board[i][j], j)
                elif board[i][j] > best3[i][1][0]:
                    best3[i][2] = best3[i][1]
                    best3[i][1] = (board[i][j], j)
                elif board[i][j] > best3[i][2][0]:
                    best3[i][2] = (board[i][j], j)
        
        res = -pow(10, 9) + (-pow(10, 9)) + (-pow(10, 9)) - 1
        for r1 in range(m):
            for j in range(3):
                val1, col1 = best3[r1][j]
                
                for r2 in range(r1+1, m):
                    for k in range(3):
                        val2, col2 = best3[r2][k]
                        if col2 == col1: continue

                        for r3 in range(r2+1, m):
                            for l in range(3):
                                val3, col3 = best3[r3][l]
                                if col3 == col1 or col3 == col2: continue

                                res = max(res, val1+val2+val3)

        return res