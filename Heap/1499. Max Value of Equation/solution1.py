class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        A = [(y-x) for x, y in points]
        B = [(x+y) for x, y in points]

        j = 0
        res = -inf
        pq1, pq2 = [], []
        for i in range(len(points)):
            while j < len(points) and points[j][0]-points[i][0] <= k:
                heapq.heappush(pq1, (-A[j], j))
                heapq.heappush(pq2, (-B[j], j))
                j += 1

            while pq1 and pq1[0][1] < i:
                heapq.heappop(pq1)
            while pq2 and pq2[0][1] < i:
                heapq.heappop(pq2)

            if pq2[0][1] != pq1[0][1]:
                res = max(res, (-pq2[0][0]) + (-pq1[0][0]))
            else:
                pop = heapq.heappop(pq1)
                while pq1 and pq1[0][1] < i:
                    heapq.heappop(pq1)
                if pq1:
                    res = max(res, (-pq2[0][0]) + (-pq1[0][0]))
                heapq.heappush(pq1, pop)
                
                pop = heapq.heappop(pq2)
                while pq2 and pq2[0][1] < i:
                    heapq.heappop(pq2)
                if pq2:
                    res = max(res, (-pq2[0][0]) + (-pq1[0][0]))
                heapq.heappush(pq2, pop)
        return res
