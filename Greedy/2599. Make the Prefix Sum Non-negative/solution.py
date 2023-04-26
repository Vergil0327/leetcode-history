from typing import List
import heapq

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        res = presum = 0
        minHeap = []
        for num in nums:
            if num >= 0:
                presum += num
            elif presum + num >= 0:
                heapq.heappush(minHeap, num)
                presum += num
            else:
                heapq.heappush(minHeap, num)
                presum += num

                x = heapq.heappop(minHeap)
                presum -= x
                res += 1

        return res
