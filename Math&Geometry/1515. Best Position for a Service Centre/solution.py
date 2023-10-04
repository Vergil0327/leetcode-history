from math import sqrt

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def getEuclidean(x, y):
            return sum(sqrt(pow(x-xx, 2) + pow(y-yy, 2)) for xx, yy in positions)

        n = len(positions)
        x = y = 0
        for xx, yy in positions:
            x += xx
            y += yy
        x /= n
        y /= n

        dist = getEuclidean(x, y)

        ## grid searching
        # set delta 100 since 0 <= positions[i][0], positions[i][1] <= 100
        delta = 100
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while delta > 1e-6:
            zoomIn = True
            for dx, dy in dirs:
                xx = x + dx*delta
                yy = y + dy*delta
                if (d := getEuclidean(xx,yy)) < dist:
                    dist = d
                    x, y = xx, yy
                    zoomIn = False
                    break # as soon as we find a point with lower objective function value, we know that the global optimum if close to that point. we can't get trapped in local optimum.
            
            # binary search
            if zoomIn: delta /= 2
        return dist
