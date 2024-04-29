class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1 # we need n-1-th element

        v = x
        idx = 0
        for i in range(64):
            if (v>>i)&1: continue
            bit = (n>>idx)&1 # bit from n-1 bitmask
            v |= bit<<i
            idx += 1
        return v
