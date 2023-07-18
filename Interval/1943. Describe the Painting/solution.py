class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        for start, end, color in segments:
            diff[start] += color
            diff[end] -= color

        res = []
        l = 0
        for r in sorted(diff.keys()):
            if diff[l] > 0: # valid starting point of interval
                res.append([l, r, diff[l]])
            diff[r] += diff[l]
            l = r
        return res
