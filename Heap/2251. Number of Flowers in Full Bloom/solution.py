class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()

        m, n = len(flowers), len(people)
        res = [0] * n
        fullbloom = [] # minHeap
        j = 0
        for date, i in sorted([date, i] for i, date in enumerate(people)):
            while j < m and flowers[j][0] <= date:
                heapq.heappush(fullbloom, flowers[j][1])
                j += 1
            while fullbloom and fullbloom[0] < date:
                heapq.heappop(fullbloom)
            res[i] = len(fullbloom)
        return res
