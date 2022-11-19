# Monotone Chain: nlogn
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees
        
        trees.sort()
        
        # corss product: pq x qr > 0 -> counter-clockwise direction
        #                        < 0 -> clockwise direction
        #                        = 0 -> collinear
        # | qx-px qy-py |
        # | rx-qx ry-qy |
        def orientation(p, q, r):
            px, py = p[0], p[1]
            qx, qy = q[0], q[1]
            rx, ry = r[0], r[1]
            return (qy-py) * (rx-qx) - (qx-px) * (ry-qy)
        
        lowerHull = [] # find right-most (in counter-clockwise)
        for point in trees:
            while len(lowerHull) >= 2 and orientation(lowerHull[-2], lowerHull[-1], point) < 0:
                lowerHull.pop()
            lowerHull.append(point)
        
        upperHull = [] # find left-most (in clockwise)
        for p in reversed(trees):
            while len(upperHull) >= 2 and orientation(upperHull[-2], upperHull[-1], p) < 0:
                upperHull.pop()
            upperHull.append(p)
        
        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the
        # beginning of the other list.
        # return lower[:-1] + upper[:-1]
        # Also don't forget to remove redundant elements from the stack (use set)
        return list(set(map(tuple, lowerHull[:-1]+upperHull[:-1])))
