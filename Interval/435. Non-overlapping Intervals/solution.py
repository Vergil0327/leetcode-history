# Greedy
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt = 0
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if i > 0 and start < intervals[i-1][1]:
                intervals[i][1] = intervals[i-1][1]
                cnt += 1
        return cnt