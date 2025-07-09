class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        if endTime[-1] != eventTime:
            startTime += [eventTime]
            endTime += [eventTime]
        if startTime[0] != 0:
            startTime = [0] + startTime
            endTime = [0] + endTime

        spaces = []
        for i in range(len(startTime)-1):
            spaces.append(startTime[i+1] - endTime[i])
        
        res = duration = 0
        j = 0
        for i in range(len(spaces)):
            duration += spaces[i]
            if i-j+1 > k+1:
                duration -= spaces[j]
                j += 1

            res = max(res, duration)
        return res
