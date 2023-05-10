# direction order: to-right -> to-bottom -> to-left -> to-top
# keep moving when next position is valid
# total moves: n*n-1
# starting with (row, column, current direction) = (0,0,0) and mat[0][0] = 1
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]

        mat[0][0] = 1
        pos = [0, 0, 0] # row, col, dir
        directions = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        for _ in range(n*n-1):
            r, c, d = pos
            dr, dc = directions[d]
            row, col = r+dr, c+dc

            while 0 <= row < n and 0 <= col < n and mat[row][col] == 0:
                mat[row][col] = mat[r][c]+1

                pos = [row, col, d]
                r, c, d = pos
                row, col = r+dr, c+dc

            pos[2] = (pos[2] + 1)%4
        return mat
