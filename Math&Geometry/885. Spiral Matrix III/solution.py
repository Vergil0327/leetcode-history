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