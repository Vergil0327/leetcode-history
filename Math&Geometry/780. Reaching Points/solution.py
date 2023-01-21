class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while ty > sy and tx > sx:
            if ty > tx:
                ty %= tx
            else:
                tx %= ty
        # 最後可能 ty > sy  or tx > sx
        if ty == sy and tx >= sx and (tx-sx)%ty == 0: return True
        if tx == sx and ty >= sy and (ty-sy)%tx == 0: return True
        return False