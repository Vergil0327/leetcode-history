class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = [] # gain, p, t
        for p, t in classes:
            nxtGain = (p+1)/(t+1) - p/t
            heapq.heappush(maxHeap, [-nxtGain, p, t])

        while extraStudents:
            _, p, t = heapq.heappop(maxHeap)
            p, t = p+1, t+1
            extraStudents -= 1

            nxtGain = (p+1)/(t+1) - p/t
            heapq.heappush(maxHeap, [-nxtGain, p, t])
        
        return sum(p/t for _, p, t in maxHeap)/len(maxHeap)