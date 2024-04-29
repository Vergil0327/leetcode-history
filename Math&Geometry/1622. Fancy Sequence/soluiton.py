class Fancy:
    def __init__(self):
        self.mul, self.inc, self.mod = 1, 0, 1000000007
        self.num = []

    def append(self, val: int) -> None:
        self.num.append([val, self.mul, self.inc])

    def addAll(self, inc: int) -> None:
        self.inc += inc

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.mod
        self.inc = self.inc * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.num): return -1

        v, v_mul, v_inc = self.num[idx]
        inverse = pow(v_mul, self.mod - 2, self.mod)
        ratio = self.mul * inverse

        # (v-v_inc)%mod * inv(v_mul)%mod
        return (v * ratio - v_inc * ratio + self.inc) % self.mod