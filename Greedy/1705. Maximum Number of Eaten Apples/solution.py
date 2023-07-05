class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)

        minHeap = []
        eaten = 0
        i = 0
        while i < n:
            while minHeap and minHeap[0][0] <= i:
                heapq.heappop(minHeap)

            if apples[i] > 0:
                heapq.heappush(minHeap, [i+days[i], apples[i]])

            if minHeap:
                eaten += 1
                minHeap[0][1] -= 1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
            i += 1

        # no more growing apples
        while minHeap:
            while minHeap and minHeap[0][0] <= i:
                heapq.heappop(minHeap)

            if minHeap:
                eaten += 1
                minHeap[0][1] -= 1
                if minHeap[0][1] == 0:
                    heapq.heappop(minHeap)
            i += 1

        return eaten
