from functools import cache

class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        digits.reverse()  # dfs低位往高位處理

        # X + Y = n
        @cache
        def dfs(pos, carry, endX, endY):
            if pos >= len(digits):
                return 1 if endX and endY and carry == 0 else 0
            target = digits[pos]

            res = 0
            for dX in range(10):
                if endX and dX != 0: continue
                if not endX and dX == 0: continue

                newEndXs = [endX]
                if not endX:
                    newEndXs.append(True)

                for dY in range(10):
                    if endY and dY != 0: continue
                    if not endY and dY == 0: continue

                    total = dX+dY+carry
                    if (total%10 != target): continue

                    newEndYs = [endY]
                    if not endY:
                        newEndYs.append(True)

                    for newEndX in newEndXs:
                        for newEndY in newEndYs:
                            res += dfs(pos+1, total//10, newEndX, newEndY)
            return res
        dfs.cache_clear()
        return dfs(0, 0, False, False)
