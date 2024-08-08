class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        m, n = rows, cols

        res = [[rStart, cStart]]

        shift = 1
        while len(res) < m*n:
            r, c = rStart, cStart+shift
            length = 2*shift+1
            
            # go down
            for _ in range(length//2+1):
                if 0 <= r < m and 0 <= c < n:
                    res.append([r,c])
                r += 1
            r -= 1

            # go left
            for _ in range(length-1):
                c -= 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r,c])

            # go up
            for _ in range(length-1):
                r -= 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r,c])
            c += 1

            # go right
            for _ in range(length):
                if 0 <= r < m and 0 <= c < n:
                    res.append([r,c])
                c += 1
            c -= 1

            # go down to the origin
            for _ in range(length//2-1):
                r += 1
                if 0 <= r < m and 0 <= c < n:
                    res.append([r,c])

            # finish one circle, increment shift
            shift += 1
        return res
    
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] # right, down, left, up
        res = [[rStart, cStart]]

        r, c = rStart, cStart
        length = d = 0 # move length step in d direction
        while len(res) < rows * cols:
            if d == 0 or d == 2: length += 1 # move to right or left, length of path require extra step

            for _ in range(length):
                r += dirs[d][0]
                c += dirs[d][0]
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            d = (d+1)%4
        return res