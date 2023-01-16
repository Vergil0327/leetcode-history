class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

     # insert in front of intervals
        if newInterval[1] < intervals[0][0]:
            res = [newInterval]
            res.extend(intervals)
            return res

        # find merge position
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # insert to the last position
        if i == len(intervals):
            res.append(newInterval)
            return res

        if intervals[i][1] < newInterval[0]: # [intervals[i], newInterval]
            res.append(intervals[i])
            res.append(newInterval)
        elif newInterval[1] < intervals[i][0]: # [newInterval, intervals[i]]
            res.append(newInterval)
            res.append(intervals[i])
        else: # [merged_interval]
            intervals[i][0] = min(intervals[i][0], newInterval[0])
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            res.append(intervals[i])

        # merge interval
        i += 1
        while i < len(intervals):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res

# Concise
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            elif newInterval[0] > interval[1]:
                res.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        res.append(newInterval)
        return res
