class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        illuminance = defaultdict(int)
        ROW, COL = 5, 10

        # remove duplicate
        LAMPS = set()
        for lamp in lamps:
            LAMPS.add(tuple(lamp))

        for i, j in LAMPS:
            # row
            illuminance[(ROW, i)] += 1
            # column
            illuminance[(COL, j)] += 1
            # diagonal
            illuminance[(1, j-i)] += 1
            illuminance[(-1, j+i)] += 1

        res = []
        for row, col in queries:
            left, right = col-1, col+1
            top, bot = row-1, row+1

            if (ROW, row) in illuminance or (COL, col) in illuminance or (1, col-row) in illuminance or (-1, col+row) in illuminance:
                res.append(1)
            else:
                res.append(0)

            for i in range(top, bot+1):
                if i < 0 or i >= n:continue
                for j in range(left, right+1):
                    if j < 0 or j >= n: continue
                    if (i, j) not in LAMPS: continue
                    LAMPS.remove((i, j))
            
                    illuminance[(ROW, i)] -= 1
                    if illuminance[(ROW, i)] == 0:
                        del illuminance[(ROW, i)]
                    illuminance[(COL, j)] -= 1
                    if illuminance[(COL, j)] == 0:
                        del illuminance[(COL, j)]
                    illuminance[(1, j-i)] -= 1
                    if illuminance[(1, j-i)] == 0:
                        del illuminance[(1, j-i)]
                    illuminance[(-1, j+i)] -= 1
                    if illuminance[(-1, j+i)] == 0:
                        del illuminance[(-1, j+i)]

        return res