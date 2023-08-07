class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxHeap = [-v for v in target]
        heapq.heapify(maxHeap)

        tot = sum(target)
        while -maxHeap[0] != 1:
            curMax = -heapq.heappop(maxHeap)

            otherSum = tot-curMax

            # TLE
            # prev = curMax - otherSum
            # if prev < 1: return False

            if otherSum == 0 or curMax <= otherSum: return False
            prev = curMax % otherSum
            if prev == 0:
                prev = otherSum
            
            tot = otherSum + prev
            
            heapq.heappush(maxHeap, -prev)
        return True