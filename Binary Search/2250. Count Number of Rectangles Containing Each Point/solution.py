class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        buckets = defaultdict(list)
        for l, h in rectangles:
           buckets[h].append(l)
        
        def count(point):
            x, y = point
            res = 0
            for h, recs in buckets.items():
                if h >= y:
                    i = bisect.bisect_left(recs, x)
                    res += len(recs) - i
            return res

        res = []
        for point in points:
            res.append(count(point))
        return res