class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(s)

        tag2points = defaultdict(list)
        for pos, tag in zip(points, s):
            tag2points[tag].append(pos)

        squareLength = lambda pos: max(abs(pos[0]), abs(pos[1]))
        for arr in tag2points.values():
            arr.sort(key=squareLength)

        boundary_len = inf
        for arr in tag2points.values():
            if len(arr) > 1:
                x, y = arr[1]
                length = max(abs(x), abs(y))
                boundary_len = min(boundary_len, length)
        

        res = 0
        for arr in tag2points.values():
            x, y = arr[0]
            length = max(abs(x), abs(y))
            if length < boundary_len:
                res += 1
        return res

