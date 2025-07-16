class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = [1]
        self.popped = set()
        

    def popSmallest(self) -> int:
        x = heapq.heappop(self.minHeap)
        if not self.minHeap:
            heapq.heappush(self.minHeap, x+1)
        self.popped.add(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.popped: return
        self.popped.remove(num)
        heapq.heappush(self.minHeap, num)
        
# 1
# minHeap = [1+1], popped = {1}
# minHeap = [2+1], popped = {1, 2}
# minHeap = [1, 3], popped = {2}
# minHeap = [3], popped = {1, 2}

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)