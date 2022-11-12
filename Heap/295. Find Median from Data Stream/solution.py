##### Intuition:

"""
It's really easy to solve this problem by `treemap`

everytime we add value, it'll take `O(logn)` to insert
since it'll be sorted after insertion, we can just get median from the middle of sorted list.
"""


from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.stream = SortedList()

	# O(logn)
    def addNum(self, num: int) -> None:
        self.stream.add(num)

	# O(1)
    def findMedian(self) -> float:
        n = len(self.stream)
        if n&1:
            return self.stream[n//2]
        else:
            return (self.stream[n//2]+self.stream[n//2-1])/2


##### MinHeap + MaxHeap

"""
as long as we always keep this relation
`num in self.small always < num in self.large`
we can find median by considering top value of these two heaps

here I do some tricks to make sure `len(self.small) is always greater than len(self.large)`, so
	1. if total is odd, top of self.small (max heap) is median
	2. if total is even, average of top element from both self.small and self.large array is median
"""

import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        if self.large and self.small and self.large[0] < -self.small[0]:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        
        while len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        while len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        n = len(self.large) + len(self.small)
        if n&1:
            return -self.small[0]
        else:
            return (-self.small[0]+self.large[0])/2