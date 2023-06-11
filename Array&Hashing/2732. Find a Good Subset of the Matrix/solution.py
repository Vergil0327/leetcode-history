class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        rows = defaultdict(int)
        for i in range(m):
            bitmask = 0
            for j in range(n):
                bitmask |= (grid[i][j]<<j)
            if bitmask == 0: return [i]
            rows[bitmask] = i

        for bitmask1, i in rows.items():
            for bitmask2, j in rows.items():
                if i == j: continue
                if bitmask1 & bitmask2 == 0: return [min(i, j), max(i, j)]
        return []