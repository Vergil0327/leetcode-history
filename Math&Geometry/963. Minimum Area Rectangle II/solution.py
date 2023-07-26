class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res = inf
        seen = defaultdict(list)
        for i, (x, y) in enumerate(points):
            for j in range(i+1, len(points)):
                x0, y0 = points[j]
                midX, midY = (x+x0)/2, (y+y0)/2
                d = (x-x0)**2 + (y-y0)**2
                for point1, point2 in seen[(midX, midY, d)]:
                    x3, y3 = point1[0], point1[1]
                    x4, y4 = point2[0], point2[1]
                    a = (x-x3)**2 + (y-y3)**2
                    b = (x-x4)**2 + (y-y4)**2
                    res = min(res, sqrt(a)*sqrt(b))

                seen[(midX, midY, d)].append([(x,y), (x0, y0)])
        return res if res != inf else 0
