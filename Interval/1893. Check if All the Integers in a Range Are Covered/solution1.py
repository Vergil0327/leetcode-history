class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        merge = []
        for l, r in ranges:
            if not merge:
                merge.append([l, r])
            else:
                if l <= merge[-1][1]+1:
                    merge[-1][1] = max(merge[-1][1], r)
                else:
                    merge.append([l, r])

        for l, r in merge:
            if left >= l and right <= r: return True
        return False