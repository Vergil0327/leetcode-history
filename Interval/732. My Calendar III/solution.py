from sortedcontainers import SortedList

class MyCalendarThree:

    def __init__(self):
        self.timeline = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline.add([startTime, 1])
        self.timeline.add([endTime, -1])

        res = cur = 0
        for t, overlap in self.timeline:
            cur += overlap
            res = max(res, cur)
        return res

class MyCalendarThree:

    def __init__(self):
        self.timeline = []

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline.append([startTime, 1])
        self.timeline.append([endTime, -1])

        res = cur = 0
        for t, overlap in sorted(self.timeline):
            cur += overlap
            res = max(res, cur)
        return res
