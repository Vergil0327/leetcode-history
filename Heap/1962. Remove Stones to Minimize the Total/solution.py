class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-p for p in piles]
        heapq.heapify(maxHeap)

        while k:
            p = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -ceil(p/2))
            k -= 1
        return -sum(maxHeap)