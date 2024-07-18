class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if (i, j) in points: continue
                    if (i-x)**2 + (j-y)**2 <= r**2:
                        points.add((i, j))
        return len(points)

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = 0
        for i in range(201):
            for j in range(201):
                for x, y, r in circles:
                    if (x-i)**2 + (y-j)**2 <= r * r:
                        res += 1
                        break
        return res