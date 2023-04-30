class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def calCost(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        res = calCost(start[0], start[1], target[0], target[1])
        pq = [(0, start)]
        visited = set()
        while pq:
            cost, (x,y) = heapq.heappop(pq)
            if (x,y) in visited: continue
            visited.add((x,y))
            res = min(res, cost + calCost(x, y, target[0], target[1]))

            for x1, y1, x2, y2, c in specialRoads:
                heapq.heappush(pq, (cost+calCost(x1, y1, x, y)+c, (x2,y2)))
        return res