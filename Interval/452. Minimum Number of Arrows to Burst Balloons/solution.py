class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by startTime in increasing order, then endTime in decreasing order
        points.sort(key=lambda x:(x[0],-x[1]))

        cnt = 0
        for i in range(len(points)):
            if i > 0 and points[i][0] <= points[i-1][1]:
                # shot the left-most overlapping points of endTime
                points[i][1] = min(points[i-1][1], points[i][1])
                continue
            else:
                cnt += 1
        return cnt

# Concise
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by endTime in increasing order
        points.sort(key=lambda x:x[1])

        cnt = 0
        for i in range(len(points)):
            startTime = points[i][0]
            if i > 0 and startTime <= points[i-1][1]:
                # shot the left-most overlapping points of endTime
                points[i][1] = points[i-1][1]
            else:
                cnt += 1
        return cnt