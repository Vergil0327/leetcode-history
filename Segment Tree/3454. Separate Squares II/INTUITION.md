# Intuition

very hard problem (Accepted 1.3K, Submissions 8.6K, Acceptance Rate 14.8% after 3~4 days)

here is the solution I think the most precise and clear.

the core idea is: sweepline + segment tree

1. iterate squares, and record y-axis change-event. [y-pos, direction (1 means left endpoint go up, -1 means right endpoint go down), left endpoint x1, right endpoint x2]

```py
events = [] # [y, 1 if go up else -1, x1, x2]
xAxis = set()
for x, y, l in squares:
    events.append((y, 1, x, x+l))
    events.append((y+l, -1, x, x+l))
    xAxis.add(x)
    xAxis.add(x+l)
xAxis = list(sorted(xAxis))
events.sort(key=lambda e: (e[0], -e[1])) # sort by y position, if y is the same, sort by direction
```

2. calculate total area covered by all squares. (use segment tree + binary search)

sweep y-axis
for each event, we know x-axis range [x1, x2] and y's pos and direction
also record previous y pos, then we can know the difference of y, `dy`

if dy > 0, it means we are sweeping up, so we can add the covered area, where covered area can be calculated by segment tree
after that, update this event to segment tree. (use binary search to find position of x1 and x2)

```py
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
```

3. find the split line. (use segment tree + binary search)

same idea with calculate total area using bianry search + sweepline + segment tree
our target is half total area, so we can sweepline in the same way and keep recording current area until we find **our current area >= half total area**


if the covered area we can add plus current area is more than half total area, then we know we are in the split line position.

- actual need area = half total area - current area
- dy = need area / covered x-axis
- split line y position = prev_y + dy

```py
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
```