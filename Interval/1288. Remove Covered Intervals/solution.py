# Sorting
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x:(x[0], -x[1]))
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                _, prevEnd = res[-1]
                if end <= prevEnd:
                    continue
                else:
                    res.append([start, end])
        return len(res)

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        prevStart, prevEnd = intervals[0][0], intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if end <= prevEnd:
                cnt += 1
            elif start <= end:
                prevEnd = end
            else:
                prevStart, prevEnd = start, end
        return len(intervals) - cnt