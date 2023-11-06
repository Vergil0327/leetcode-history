class Bit:
    def __init__(self, op, e, n):
        self.op = op
        self.e = e
        self.n = n+1
        self.table = [e() for _ in range(self.n)]

    def update(self, i, x):
        i += 1
        while i < self.n:
            self.table[i] = self.op(self.table[i], x)
            i += i & -i

    def prod(self, i):
        i += 1
        res = self.e()
        while i > 0:
            res = self.op(res,self.table[i])
            i -= i & -i
        return res
