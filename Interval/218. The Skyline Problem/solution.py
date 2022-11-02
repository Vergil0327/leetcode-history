# SweepLine with MaxHeap
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # rising edge(上升沿): add new height at current sweepline position
        # falling edge(下降沿): remove sweepline height at current position
        arr = sorted([x for L,R,H in buildings for x in [[L,-H,R],[R,0,0]]])

        res = []
        maxHeap = [] # [-height, R(end position)]
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

from sortedcontainers import SortedList

# Sweepline algorithm with sorted list
# O(nlog(n))
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        maxHeight = SortedList(key=lambda item: (-item[0], item[1])) # [height, position]
        
        # sort in increasing order of left first
        # then sort in decreasing order of height. we need to push current building's height to maxHeight list prior to pop out invalid current max-height
        timeline = sorted([x for L, R, H in buildings for x in [[L, H, R],[R,0,0]]], key= lambda arr: (arr[0], -arr[1], arr[2]))

        res = []
        for pos, height, R in timeline:
            if R == 0:
                while maxHeight and maxHeight[0][1] <= pos:
                    maxHeight.pop(0)
            
            if height != 0:
                maxHeight.add([height, R])
            
            if maxHeight:
                if not res or res[-1][1] != maxHeight[0][0]:
                    res.append([pos, maxHeight[0][0]])
            else:
                if not res or res[-1][1] != 0:
                    res.append([pos, 0])
        return res