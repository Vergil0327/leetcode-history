# Sweepline
class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(first) and j < len(second):
            if first[i][1] < second[j][0]: # skip non-overlapping
                i += 1
            elif second[j][1] < first[i][0]: # skip non-overlapping
                j += 1
            else:
                # find whose start time is smaller, we always compare smallest start time interval with the other
                # after comparison, skip current smallest start time and sweepline goes on
                if first[i][0] < second[j][0]:
                    res.append([max(first[i][0], second[j][0]), min(first[i][1], second[j][1])])
                    if first[i][1] < second[j][1]:
                        i += 1
                    else:
                        j += 1
                else:
                    res.append([max(first[i][0], second[j][0]), min(first[i][1], second[j][1])])
                    if first[i][1] < second[j][1]:
                        i += 1
                    else:
                        j += 1
        return res

class ConciseSolution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0],secondList[j][0])
            hi = min(firstList[i][1],secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j +=1
        return ans
