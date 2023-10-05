class SORTracker:

    def __init__(self):
        from sortedcontainers import SortedList
        self.call = -1
        self.sor = SortedList()

    def add(self, name: str, score: int) -> None:
        self.sor.add([-score, name])
        
    def get(self) -> str:
        self.call += 1
        return self.sor[self.call][1]

from heapq import *

class MinHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score < other.score or \
               (self.score == other.score and self.name > other.name)

class MaxHeapItem:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        return self.score > other.score or \
               (self.score == other.score and self.name < other.name)

class SORTracker:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def add(self, name: str, score: int) -> None:
        heappush(self.minHeap, MinHeapItem(name, score))

        item = heapq.heappop(self.minHeap)
        heappush(self.maxHeap, MaxHeapItem(item.name, item.score))
            
    def get(self) -> str:

        item = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, MinHeapItem(item.name, item.score))
        return item.name