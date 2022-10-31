class MyCalendar:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> bool:
        # O(log(n))
        # l, r = 0, len(self.list)
        # while l < r:
        #     mid = l + (r-l)//2
        #     if self.list[mid][0] > start:
        #         r = mid
        #     else:
        #         l = mid+1
        # idx = l
        idx = bisect.bisect_right(self.list, [start, end])

        if idx-1 >=0 and self.list[idx-1][1] > start:
            return False
        if idx < len(self.list) and self.list[idx][0] < end:
            return False

        # O(k+n)
        self.list[idx:idx] = [[start, end]]
        return True

from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.list = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.list.bisect_right([start, end])
        if idx < len(self.list) and self.list[idx][0] < end:
            return False
        if idx > 0 and self.list[idx-1][1] > start:
            return False

        self.list.add([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
