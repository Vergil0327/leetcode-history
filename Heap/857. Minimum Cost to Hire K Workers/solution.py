class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        arr = sorted(zip(wage, quality), key=lambda x:x[0]/x[1])

        pq = []
        quality_k_sum = 0
        res = inf
        for w, q in arr:
            quality_k_sum += q
            if len(pq) == k-1:
                res = min(res, (w/q) * quality_k_sum)
            
            heapq.heappush(pq, -q)
            if len(pq) == k:
                quality_k_sum -= -heapq.heappop(pq)
        return res
