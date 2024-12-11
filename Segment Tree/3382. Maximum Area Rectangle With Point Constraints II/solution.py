class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = list(zip(xCoord, yCoord))

        # sort by x, then y
        points.sort()
        yAxis = sorted(set(yCoord))
        yPos = {y: i for i, y in enumerate(yAxis)}
        yMax = {y: -inf for y in yAxis}
        maxTree = SegmentTree(len(yAxis))
        prevX, prevY = points[0]
        res = -1

        for x, y in points[1:]:
            if (
                prevX == x
                and yMax[prevY] == yMax[y]
                and yMax[y] > maxTree.query(yPos[prevY], yPos[y])
            ):
                # x's and y's are aligned
                # and no other points in the rectangle
                res = max(res, (y - prevY) * (x - yMax[y]))

            # update the info of (prevX, prevY)
            yMax[prevY] = max(yMax[prevY], prevX)
            maxTree[yPos[prevY]] = yMax[prevY]
            prevX, prevY = x, y
        return res


class SegmentTree:

    def __init__(self, n: int):
        self.n = n
        self.tree = [-inf] * (self.n << 1)

    def __getitem__(self, i):
        return self.tree[i+self.n]

    def __setitem__(self, i, v):
        tree, n = self.tree, self.n
        i += n
        tree[i] = v

        while i:
            tree[i>>1] = max(tree[i], tree[i^1])
            i >>= 1

    def query(self, l: int, r: int) -> int:
        res = -inf
        l += self.n
        r += self.n
        while r - l > 1:
            if not l & 1:
                res = max(res, self.tree[l + 1])
            if r & 1:
                res = max(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
