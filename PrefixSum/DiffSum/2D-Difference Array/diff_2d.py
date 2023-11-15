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
