# # Intuition

# greedily use minimum cost worker to reduce mountain height
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        pq = [[t*1, t, 1] for t in workerTimes]
        heapq.heapify(pq)

        while mountainHeight:
            cost, t, x = heapq.heappop(pq)
            mountainHeight -= 1
            x += 1

            # t*1 + t*2 + t*3 + ... + t*x = t * (1+2+...+x) = t * ((1+x) * x // 2)
            new_cost = t * ((1+x) * x // 2)

            heapq.heappush(pq, [new_cost, t, x])
        
        return max(cst - t*x for cst, t, x in pq)
