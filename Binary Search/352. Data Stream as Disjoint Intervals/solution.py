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

from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.intervals = SortedSet()

    def addNum(self, value: int) -> None:
        self.intervals.add(value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        l, r = -1, -1
        for num in self.intervals:
            if l < 0:
                l = r = num
            elif num == r+1:
                r = num
            else:
                res.append([l, r])
                l = r = num
        res.append([l, r])
        return res

# Min Heap
class SummaryRanges(object):

  def __init__(self):
    self.intervals = []
    self.has = set()
    
  def addNum(self, val):
    if val in self.has: return

    self.has.add(val)
    heapq.heappush(self.intervals, [val, [val, val]])
    
  def getIntervals(self):
    stack = []
    while self.intervals:
        priority, interval = heapq.heappop(self.intervals)

        if not stack:
            stack.append([priority, interval])
        else:
            prevInterval = stack[-1][1]
            if prevInterval[1] + 1 >= interval[0]:
                prevInterval[1] = max(prevInterval[1], interval[1])
            else:
                stack.append([priority, interval])
    
    self.intervals = stack
    return list(map(lambda arr:arr[1], stack))