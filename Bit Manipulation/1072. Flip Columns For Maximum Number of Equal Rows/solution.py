class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = defaultdict(int)
        for row in matrix:
            vals = []
            flips = []
            for col in row:
                vals.append(col)
                flips.append(1-col)
            cache[tuple(vals)] += 1
            cache[tuple(flips)] += 1

        return max(cache.values())
