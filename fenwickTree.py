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







class Fenwick:
    def __init__(self, n):
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < len(self.a):
            self.a[i] += x
            i += i & -i


