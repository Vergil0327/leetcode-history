from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(-x[1], x[0]))
        n = len(points)
        res = 0
        for i in range(n):
            x1, y1 = points[i]
            sl = SortedList()
            for j in range(i+1, n):
                x2, y2 = points[j]
                if x2 < x1: continue
                
                l = sl.bisect_left(x1)
                r = sl.bisect_right(x2)-1
                if r-l+1 == 0:
                    res += 1
                sl.add(x2)
        return res
