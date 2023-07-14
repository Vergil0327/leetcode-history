class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        minHeap = []
        if ladders >= n-1: return n-1

        i = 0
        while ladders and i+1 < n:
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heapq.heappush(minHeap, diff)
                ladders -= 1
            i += 1

        while i+1 < n:
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heapq.heappush(minHeap, diff)
                bricks -= heapq.heappop(minHeap)
                if bricks < 0: return i
            i += 1
        return i
