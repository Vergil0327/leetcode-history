# Binary Search
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.has = set()

    def addNum(self, value: int) -> None:
        if value in self.has: return
        self.has.add(value)

        # O(logn)
        intervals = self.intervals
        l, r = 0, len(intervals)
        while l < r:
            mid = l + (r-l)//2
            if intervals[mid][1] < value:
                l = mid+1
            else:
                r = mid

        # O(n)
        if l == len(intervals):
            intervals.append([value, value])
        else:
            intervals.insert(l, [value, value])

        # Merge Intervals O(n)
        res = []
        for start, end in intervals:
            if not res:
                res.append([start,end])
            else:
                if start > res[-1][1]+1:
                    res.append([start, end])
                else:
                    res[-1][1] = end
        self.intervals = res

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

from sortedcontainers import SortedList