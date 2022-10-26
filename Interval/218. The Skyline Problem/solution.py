# SweepLine with MaxHeap
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # rising edge(上升沿): add new height at current sweepline position
        # falling edge(下降沿): remove sweepline height at current position
        arr = sorted([x for L,R,H in buildings for x in [[L,-H,R],[R,0,0]]])

        res = []
        maxHeap = [] # [-height, R(end-position)]
        for pos, negHeight, R in arr:
            # check if we need to remove current max height at each falling edge
            while maxHeap and maxHeap[0][1] <= pos:
                heapq.heappop(maxHeap)

            # add height to maxHeap when current iteration is at rising edge position
            if negHeight != 0:
                heapq.heappush(maxHeap, (negHeight, R))
          
            # if current max height equals to previous one,
            # we don't need to append
            # we can optimized by add fallback value to res & maxHeap
            # ex.
            #   [0, float('inf')] is always in max_heap, so max_heap[0] is always valid
            #   res, max_heap = [[0, 0]], [[0, float('inf')]]
            #   ...
            #   return res[1:]
            if maxHeap:
                currMaxHeight = -maxHeap[0][0]
                if not res or res[-1][1] != currMaxHeight:
                    res.append([pos, currMaxHeight])
            else: # current max height is ground zero
                if not res or res[-1][1] != 0:
                    res.append([pos, 0])

        return res