class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append([max(0, i-r), min(n, i+r)])
        intervals.sort()

        m = len(intervals)
        res = i = j = 0
        while i < n:
            nextPos = i
            while j < m and intervals[j][0] <= i:
                nextPos = max(nextPos, intervals[j][1])
                j += 1

            if i == nextPos: return -1
            i = nextPos
            res += 1
        return res