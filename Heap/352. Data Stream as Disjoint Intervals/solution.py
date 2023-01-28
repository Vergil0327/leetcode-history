class SummaryRanges(object):

    def __init__(self):
        self.intervals = []
        self.has = set()
    
    def addNum(self, val):
        if val in self.has: return
        self.has.add(val)
        heapq.heappush(self.intervals, [val, val])
    
    def getIntervals(self):
        res = []
        while self.intervals:
            start, end = heapq.heappop(self.intervals)
            if not res or start > res[-1][1]+1:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        self.intervals = res
        return res

from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.intervals = SortedSet()

    def addNum(self, value: int) -> None:
        self.intervals.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        l, r = -1, -1
        for num in intervals:
            if l == -1:
                l = r = num
            elif num+1 == r:
                r = num
            else:
                res.append([l, r])
                l = r = num
        res.append([l, r])
        return res

class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.has = set()

    def addNum(self, value: int) -> None:
        if value in self.has: return

        self.has.add(value)
        intervals = self.intervals
        l, r = 0, len(intervals)
        while l < r:
            mid = l + (r-l)//2
            if intervals[mid][1] < value:
                l = mid+1
            else:
                r = mid

        if l == len(intervals):
            intervals.append([value, value])
        else:
            intervals.insert(l, [value, value])

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