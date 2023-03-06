class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for tp in timePoints:
            [hr, minute] = tp.split(":")
            times.append(int(hr)*60+int(minute))

        times.sort()
        times.append(times[0]+60*24)
        
        diff = inf
        for i in range(len(times)-1):
            a, b = times[i], times[i+1]
            diff = min(diff, min(b-a, 60*24-(b-a)))            
        
        return diff
    
# Concise
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [int(tp[:2])*60 + int(tp[3:]) for tp in timePoints]

        times.sort()
        HOURS_24 = 60*24
        diff = (times[0] + HOURS_24) - times[-1]
        for i in range(len(times)-1):
            d = times[i+1]-times[i] # clockwise, and HOURS_24-d is counter-clockwise
            diff = min(diff, d, HOURS_24-d)
        return diff