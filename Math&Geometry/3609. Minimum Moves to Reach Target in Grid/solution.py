class Solution:
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if (sx==tx and sy==ty): return 0
        if (tx<sx or ty<sy): return -1

        if tx > ty:
            if tx >= 2*ty:
                if tx%2 == 0:
                    step = self.minMoves(sx, sy, tx//2, ty)
                    return 1+step if step > -1 else -1
                else:
                    return -1
            else:
                step = self.minMoves(sx, sy, tx-ty, ty)
                return 1+step if step > -1 else -1
        elif tx < ty:
            return self.minMoves(sy, sx, ty, tx)
        else:
            step = self.minMoves(sx, sy, 0, tx)
            if step > -1:return 1+step
            step = self.minMoves(sx, sy, tx, 0)
            if step > -1: return 1+step
            return -1
