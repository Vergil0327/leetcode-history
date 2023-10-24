class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        # a sub function that calculates the center of the circle
        def circles_from_p1p2r(p1, p2, r):
            (x1, y1), (x2, y2) = p1, p2

            # delta x, delta y between points
            dx, dy = x2 - x1, y2 - y1

            # dist between points
            q = math.sqrt(dx**2 + dy**2)

            # if two points are too far away, there is no such circle
            if q > 2.0*r:
                return []

            # find the halfway point
            x3, y3 = (x1+x2)/2, (y1+y2)/2

            # distance along the mirror line
            d = math.sqrt(r**2-(q/2)**2)

            # One circle
            c1 = [x3 - d*dy/q, y3 + d*dx/q]

            # The other circle
            c2 = [x3 + d*dy/q, y3 - d*dx/q]
            return [c1, c2]

        res = 1 # 1 point at least
        n = len(points)

        for p in range(n):
            for q in range(p+1, n):

                # Find candidate circle for each pair of points
                TwoCirs = circles_from_p1p2r(points[p], points[q], r)

                # count how many dots are inside the circle
                for x0, y0 in TwoCirs:
                    cnt = 0
                    for x, y in points:
                        if (x-x0)**2 + (y-y0)**2 - r**2 <= 1e-6:
                            cnt += 1
                    res = max(res, cnt)
                        
        return res
