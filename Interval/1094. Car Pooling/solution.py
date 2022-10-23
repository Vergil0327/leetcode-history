# Sweep Line algorithm
# see Meeting Rooms II: https://www.youtube.com/watch?v=FdzJmTCVyJU

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # (position, capicity)
        starts = sorted([[trip[1], trip[0]] for trip in trips])
        ends = sorted([trip[2], trip[0]] for trip in trips)

        i, j = 0, 0 # pointer for pick-up & drop-off
        cap = 0
        while i < len(starts):
            pickupPos = starts[i][0]
            dropoffPos = ends[j][0]
            if pickupPos < dropoffPos: # pick up
                cap += starts[i][1]
                i += 1
            else: # drop off
                cap -= ends[j][1]
                j += 1
            if cap > capacity:
                return False
        return True

# https://leetcode.com/problems/car-pooling/discuss/317610/JavaC%2B%2BPython-Meeting-Rooms-III
class ConciseSolution:
    def carPooling(self, trips, capacity):
        for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, - n]]):
            capacity -= v
            if capacity < 0:
                return False
        return True

class ConciseSolution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # (position, capicity)
        timeline = sorted(x for cap, start, end in trips for x in [[start, cap], [end, -cap]])
        
        currCap = 0
        for _, cap in timeline:
            currCap += cap
            if currCap > capacity:
                return False
        return True
