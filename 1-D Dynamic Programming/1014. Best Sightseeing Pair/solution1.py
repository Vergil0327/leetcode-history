class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        pq = []
        for i in range(n-1):
            heapq.heappush(pq, [-(values[i]+i), i])
        
        res = 0
        for j in range(n-1, 0, -1):
            cur = values[j]-j
            # find max(values[i]+i in values[:j])
            while pq and pq[0][1] >= j:
                heapq.heappop(pq)
            res = max(res, cur + (-pq[0][0]))
            
        return res
