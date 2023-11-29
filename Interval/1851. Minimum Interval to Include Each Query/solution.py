class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        res = [-1]*len(queries)
        minHeap = []
        i = 0
        for t, idx in sorted([[q, i] for i, q in enumerate(queries)]):
            while i < len(intervals) and intervals[i][0] <= t:
                left, right = intervals[i]
                heapq.heappush(minHeap, [right-left+1, left, right])
                i += 1
            while minHeap and minHeap[0][2] < t:
                heapq.heappop(minHeap)
            if minHeap:
                res[idx] = minHeap[0][0]
        return res