class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
                
        maxHeap = []
        res = l = r = 0
        windowsum = 0
        while r < n:
            windowsum += runningCosts[r]
            heapq.heappush(maxHeap, [-chargeTimes[r], r])
            r += 1

            while l < r and (cost := -maxHeap[0][0] + (r-l) * windowsum) > budget:
                windowsum -= runningCosts[l]
                l += 1
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)

            res = max(res, r-l)
        return res