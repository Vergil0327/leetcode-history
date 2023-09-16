class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        pq = []
        
        for num, cnt in count.items():
            heapq.heappush(pq, -cnt)

        while len(pq)>1:
            cnt1 = -heapq.heappop(pq)
            cnt2 = -heapq.heappop(pq)
            cnt1 -= 1
            cnt2 -= 1
            if cnt1 > 0:
                heapq.heappush(pq, -cnt1)
            if cnt2 > 0:
                heapq.heappush(pq, -cnt2)

        return -sum(pq)