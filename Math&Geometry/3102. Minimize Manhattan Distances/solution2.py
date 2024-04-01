from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        SUM, DIFF = SortedList(), SortedList()
        for x, y in points:
            SUM.add(x+y)
            DIFF.add(x-y)

        res = inf
        for x, y in points:
            SUM.remove(x+y)
            DIFF.remove(x-y)
            res = min(res, max(SUM[-1]-SUM[0], DIFF[-1]-DIFF[0]))
            SUM.add(x+y)
            DIFF.add(x-y)
        return res