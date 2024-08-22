class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bit = 0
        self.cnt = 0

    def fix(self, idx: int) -> None:
        if (self.bit>>idx)&1: return
        self.cnt += 1
        self.bit |= 1<<idx
        

    def unfix(self, idx: int) -> None:
        if (self.bit>>idx)&1:
            self.bit ^= 1<<idx
            self.cnt -= 1
        

    def flip(self) -> None:
        mask = (1<<self.size)-1
        self.bit ^= mask
        self.cnt = self.size - self.cnt
        

    def all(self) -> bool:
        return self.cnt == self.size
        

    def one(self) -> bool:
        return self.cnt >= 1
        

    def count(self) -> int:
        return self.cnt
        

    def toString(self) -> str:
        res = bin(self.bit)[2:][::-1]

        return res.ljust(self.size, '0') # padding leading zeros
