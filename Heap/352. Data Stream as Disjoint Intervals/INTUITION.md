# Intuition

first, think what kind of data structure do we need?
1. need a sorted containers.
2. need hashset to prevent duplicate

for a sorted containers, I think both of these should work:
1. SortedList
2. minHeap (lazy sorted)

then I choose minHeap and try to implement it

it turns out the approach is straightforward:
1. add `value` to min heap as single point `[value, value]`
2. merge intervals at `def getIntervals()` and return merged result
    - merged intervals still a min heap!
    - we can directly update our minHeap with merged intervals and optimize time complexity of next call of `addNum` or `getIntervals`

# Complexity
- Time complexity:

addNum: $$O(logn)$$
getIntervals: $$O(nlogn)$$

- Space complexity:
$$O(n)$$

# Code
```
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
```