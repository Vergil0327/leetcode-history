class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        extra = 0
        angles = []
        x0, y0 = location
        for x, y in points:
            if x == x0 and y == y0:
                extra += 1
            else:
                angles.append(math.atan2(y-y0, x-x0))
        angles.sort()

        angles = angles + [x + 2.0 * math.pi for x in angles]

        angle = (angle/360) * 2*math.pi
        n = len(angles)
        res = l = r = 0
        while r < n:
            right = angles[r]
            r += 1
            while l < r and right-angles[l] > angle:
                l += 1
            res = max(res, r-l)
        return res + extra