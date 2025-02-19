class SegmentTree:
    def __init__(self, coords):
        self.xs = coords
        n = len(coords) - 1
        self.size = 4 * n
        self.count = [0] * self.size
        self.covered = [0] * self.size
        self.n = n

    def _update(self, idx, start, end, l, r, val):
        if l > end or r < start: return

        if l <= start and end <= r: # [start, end] within [l,r]
            self.count[idx] += val
        else:
            mid = (start + end) >> 1
            self._update(idx*2, start, mid, l, r, val)
            self._update(idx*2+1, mid+1, end, l, r, val)

        if self.count[idx] > 0:
            self.covered[idx] = self.xs[end+1] - self.xs[start]
        else:
            if start == end:
                self.covered[idx] = 0
            else:
                self.covered[idx] = self.covered[idx*2] + self.covered[idx*2+1]

    def update(self, l, r, val):
        self._update(1, 0, self.n-1, l, r, val)

    def total_covered(self):
        return self.covered[1]


import bisect
class Solution:
    def separateSquares(self, squares):
        # sweepline
        events = [] # [y, 1 if go up else -1, x1, x2]
        xAxis = set()
        for x, y, l in squares:
            events.append((y, 1, x, x+l))
            events.append((y+l, -1, x, x+l))
            xAxis.add(x)
            xAxis.add(x+l)
        xAxis = list(sorted(xAxis))
        events.sort(key=lambda e: (e[0], -e[1])) # sort by y position, if y is the same, sort by direction

        # calculate total area
        seg = SegmentTree(xAxis)
        total_area = 0
        prev_y = events[0][0]
        for i in range(len(events)):
            y, direction, x1, x2 = events[i]
            dy = y - prev_y
            if dy > 0:
                covered = seg.total_covered()
                total_area += covered * dy
                prev_y = y
            l = bisect.bisect_left(xAxis, x1)
            r = bisect.bisect_left(xAxis, x2) - 1
            seg.update(l, r, direction)

        # find split line
        seg = SegmentTree(xAxis)
        half = total_area / 2.0
        current_area = 0
        prev_y = events[0][0]
        for i in range(len(events)):
            y, direction, x1, x2 = events[i]
            dy = y - prev_y
            if dy > 0:
                covered = seg.total_covered()
                can_add = covered * dy
                if current_area + can_add >= half:
                    need = half - current_area
                    return prev_y + need / covered if covered != 0 else float(y)
                current_area += can_add
                prev_y = y
            l = bisect.bisect_left(xAxis, x1)
            r = bisect.bisect_left(xAxis, x2) - 1
            seg.update(l, r, direction)
        return float(prev_y)
