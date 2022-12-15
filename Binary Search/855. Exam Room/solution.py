class ExamRoom:
    def __init__(self, N):
        self.N, self.seats = N, []

    # O(n)
    def seat(self):
        N, seats = self.N, self.seats
        if not seats: res = 0
        else:
            dist, res = seats[0], 0
            # a, b: adjacent seats
            for a, b in zip(seats, seats[1:]):
                if (b - a) // 2 > dist:
                    dist = (b - a) // 2
                    res = (b + a) // 2
            if N - 1 - seats[-1] > dist: res = N - 1
        bisect.insort(seats, res)
        return res

    # O(n)
    def leave(self, p):
        self.seats.remove(p)

from sortedcontainers import SortedList
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.start = defaultdict(list)
        self.end = defaultdict(list)
        def compare(item):
            x, y = item[0], item[1]
            if x == -1: return y
            if y == n: return n-1-x
            return (y-x)//2
        self.intervals = SortedList(key=compare)
        self.intervals.add((-1, n))

    def seat(self) -> int:
        intervals = self.intervals
        l, r = intervals[0]
        
        seat = None
        if l == -1:
            seat = 0
        elif r == self.n:
            seat = self.n-1
        else:
            seat = l + (r-l)//2 # middle
        
        # break interval to two small interval
        # [l,r] -> [l,mid] & [mid,r]
        left, right = (l, seat), (seat, right)
        self.intervals.remove(intervals[0])
        
        self.intervals.add(left)
        self.start[l].append(left)
        self.end[seat].append(left)
        
        self.intervals.add(right)
        self.start[seat].append(right)
        self.end[right].append(right)
    
    def leave(self, p: int) -> None:
        # find p's left & right interval
        right = self.start[p]
        left = self.end[p]

        # merge two interval into one intervals since p will be removed
        merged = (left[0], right[1])
        
        # remove two intervals
        self.intervals.remove(left)
        del self.start[left[0]]
        del self.end[left[1]]

        self.intervals.remove(right)
        del self.start[right[0]]
        del self.end[right[1]]

        # add new merged interval
        self.intervals.add(merged)
        self.start[merged[0]].append(merged)
        self.end[merged[1]].append(merged)
