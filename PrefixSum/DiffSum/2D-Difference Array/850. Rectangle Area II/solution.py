class Diff2D:
    def __init__(self, m, n) -> None:
        self.m = m
        self.n = n

        self.diff = [[0]*(n+1) for _ in range(m+1)]
        self.result = [[0]*(n+1) for _ in range(m+1)]

    def set(self, x0, y0, x1, y1, val):
        """
        top-left: (x0, y0)
        bottom-right: (x1, y1)
        """
        diff = self.diff

        # 排容原理
        diff[x0][y0] += val
        diff[x0][y1+1] -= val
        diff[x1+1][y0] -= val
        diff[x1+1][y1+1] += val

    def compute(self):
        diff, result = self.diff, self.result

        # c b
        # a current
        result[0][0] = diff[0][0]
        for i in range(self.m):
            for j in range(self.n):
                a = result[i-1][j] if i-1 >= 0 else 0
                b = result[i][j-1] if j-1>= 0 else 0
                c = result[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                result[i][j] = a + b - c + diff[i][j]

# Difference array
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10**9 + 7

        rows = set()
        cols = set()
        for x1, y1, x2, y2 in rectangles:
            rows.add(x1)
            rows.add(x2)
            cols.add(y1)
            cols.add(y2)

        rows = sorted(list(rows))
        cols = sorted(list(cols))
        m, n = len(rows), len(cols)
        X2idx = {rows[i]: i for i in range(m)}
        Y2idx = {cols[i]: i for i in range(n)}

        diff2D = Diff2D(m, n)
        for x1, y1, x2, y2 in rectangles:
            i = X2idx[x1]
            j = Y2idx[y1]
            x = X2idx[x2]-1 # 將像素格子壓縮成點來計算面積
            y = Y2idx[y2]-1

            diff2D.set(i, j, x, y, 1)

        diff2D.compute()

        res = 0
        for i in range(m):
            for j in range(n):
                if diff2D.result[i][j] > 0:
                    # 點還原成原圖的像素格子
                    dx = rows[i+1]-rows[i]
                    dy = cols[j+1]-cols[j]
                    res = (res + dx*dy%mod)%mod
        return res
    

# Sweepline
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rows = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        X2idx = {v: i for i, v in enumerate(rows)}
        
        sweepline = []
        for x1, y1, x2, y2 in rectangles:
            sweepline.append([y1, x1, x2, 1])  #  1: start position in y-axis
            sweepline.append([y2, x1, x2, -1]) # -1: end position in y-axis
        sweepline.sort()
        
        mod = 10 ** 9 + 7
        count = [0] * len(X2idx) # count[i]: the number of overlaps on the interval [x[i], x[i + 1]]
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in sweepline:
            area += (y - cur_y) * cur_x_sum % mod
            cur_y = y
            for i in range(X2idx[x1], X2idx[x2]):
                count[i] += sig

            cur_x_sum = sum(rows[i+1]-rows[i] for i in range(len(rows)-1) if count[i] > 0)

        return area % mod