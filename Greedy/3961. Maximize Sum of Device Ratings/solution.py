import heapq
class Solution:
    """
    Best Way:
    put each device's minimum to device which has minimum 2nd-minimum
    then we get (m-1) larger devices and 1 device with all the minimum units from others
    """
    def maxRatings(self, units: List[List[int]]) -> int:
        m, n = len(units), len(units[0])
        if n == 1:
            return sum(units[i][0] for i in range(m))

        min1 = []
        min2 = []
        for i in range(m):
            minHeap = []
            for j in range(n):
                heapq.heappush(minHeap, units[i][j])
            min1.append(heapq.heappop(minHeap))
            min2.append(heapq.heappop(minHeap))

        min2.sort()
        return min(min1) + sum(min2[1:])
    
    