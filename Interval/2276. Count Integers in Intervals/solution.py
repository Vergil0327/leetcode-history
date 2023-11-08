from sortedcontainers import SortedDict
class CountIntervals:

    def __init__(self):
        self.intervals = SortedDict()
        self.cnt = 0
        

    def add(self, left: int, right: int) -> None:
        intv = self.intervals
        j = intv.bisect_right(right)
        while j-1 >= 0 and intv.peekitem(j-1)[1] >= left:
            left = min(left, intv.peekitem(j-1)[0])
            right = max(right, intv.peekitem(j-1)[1])
            self.cnt -= intv.peekitem(j-1)[1] - intv.peekitem(j-1)[0] + 1
            intv.popitem(j-1)
            j -= 1
        intv[left] = right
        self.cnt += right-left+1

    def count(self) -> int:
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
