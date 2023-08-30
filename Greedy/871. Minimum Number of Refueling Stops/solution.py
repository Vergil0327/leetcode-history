class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            return 0 if startFuel >= target else -1
        
        if startFuel >= target: return 0

        pos = startFuel
        res = i = 0
        maxHeap = []
        while pos < target:
            while i < len(stations) and stations[i][0] <= pos:
                heapq.heappush(maxHeap, [-stations[i][1], i])
                i += 1

            if not maxHeap: return -1
            pos += -heapq.heappop(maxHeap)[0]
            res += 1
        return res
