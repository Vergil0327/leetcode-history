from sortedcontainers import SortedList
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = SortedList() # [r, l, height]
        maxH = 0
        res = []
        for l, length in positions:
            r = l+length
            
            endIdx = intervals.bisect_right([r, -inf, -inf])
            h = 0
            for i in range(endIdx):
                left, right, height = intervals[i]
                if right < l: continue
                h = max(h, height)
            h += length

            intervals.add([l, r-1, h])
            maxH = max(maxH, h)
            res.append(maxH)
        return res
