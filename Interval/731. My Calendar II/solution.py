from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.time = SortedList()

    def book(self, start: int, end: int) -> bool:
        overlap = [] # overlap with [start, end)
        for time in self.time:
            if time[1] <= start: continue
            if time[0] >= end: break
            overlap.append(time)

        for i in range(1, len(overlap)):
            if overlap[i-1][1] > overlap[i][0]: return False
        
        self.time.add((start, end))
        return True

# credit to https://leetcode.com/problems/my-calendar-ii/solutions/109530/n-2-python-short-and-elegant
class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i: # double-booking overlap with [start, end)
                return False

        for i, j in self.calendar:
            if start < j and end > i: # overlap with [start, end)
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))
        return True