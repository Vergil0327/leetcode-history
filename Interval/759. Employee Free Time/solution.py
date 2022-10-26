import heapq
from typing import List, Optional


# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]

class Solution:
    def solution(self, schedule) -> List[List]:
        # [1,3],[2,4],[2,5],[6,7],[9,12]
        # [1,3,True] [2,4,True] [2,5,True] [3,0,False] [4,0,False] [5,0,False] [6,7,True][7,0,False] [9,12,True] [12,0,False]
        # [start, end, still exists]
        arr = sorted([x for interval in schedule for start, end in interval for x in [[start, end, True], [end, 0, False]]])
        minH = []
        res = []

        freeTimeStart = float("-inf")
        for start,end,hasSchedule in arr:
            if hasSchedule:
                # empty means free time exists before current schedule
                if not minH and freeTimeStart != float("-inf"):
                    res.append([freeTimeStart, start])

                heapq.heappush(minH, [start, end])
            else:
                while minH and minH[0][1] <= start:
                    _, end = heapq.heappop(minH)
                    freeTimeStart = end
        return res
    
    # merge interval
    def solution2(self, schedule) -> List[List]:
        arr = sorted([x for interval in schedule for x in interval])

        res = []
        intervals = []
        for start,end in arr:
            if not intervals or start > intervals[-1][1]:
                if intervals:
                    res.append([intervals[-1][1], start])

                intervals.append([start, end])
            else:
                intervals[-1][1] = max(intervals[-1][1], end)
        return res
    
    def solution2_optimized(self, schedule) -> List[List]:
        arr = sorted([x for interval in schedule for x in interval])

        res = []
        intervals = arr[0]
        for start,end in arr:
            if start > intervals[1]:
                if intervals:
                    res.append([intervals[1], start])

                intervals=[start, end]
            else:
                intervals[1] = max(intervals[1], end)
        return res

        # 1---------3
        #     2-------------4
        #     2-----------------------5
        #                                     6-------7
        #                                                     9--------12