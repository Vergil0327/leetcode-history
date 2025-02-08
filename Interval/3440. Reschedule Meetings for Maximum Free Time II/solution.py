from sortedcontainers import SortedList
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime += [eventTime]
        endTime += [eventTime]
        n = len(startTime)

        gaps = SortedList()
        gaps_after = SortedList()
        for i in range(n-1):
            gaps_after.add(startTime[i+1] - endTime[i])

        res = prev = 0
        for i in range(n):
            duration = endTime[i] - startTime[i]
            gap = startTime[i] - prev
            
            if i+1<n:
                gaps_after.remove(startTime[i+1]-endTime[i])

            if gaps.bisect_left(duration) < len(gaps) or gaps_after.bisect_left(duration) < len(gaps_after):
                res = max(res, gap + duration + (startTime[i+1]-endTime[i] if i+1<n else 0))
            else:
                res = max(res, gap + (startTime[i+1]-endTime[i] if i+1<n else 0))

            gaps.add(gap)
            prev = endTime[i]
        return res
    
# optimization
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[i] - (endTime[i-1] if i > 0 else 0) for i in range(len(startTime))]
        gaps.append(eventTime - endTime[-1])
        
        prefix_max = [0]
        for gap in gaps[:-1]:
            prefix_max.append(max(prefix_max[-1], gap))
        
        suffix_max = [0]
        for gap in reversed(gaps[1:]):
            suffix_max.append(max(suffix_max[-1], gap))
        suffix_max = suffix_max[::-1]
        
        max_gap = max(gaps)
        for i in range(len(startTime)):
            duration = endTime[i] - startTime[i]
            left_gap = gaps[i]
            right_gap = gaps[i+1]
            max_gap = max(max_gap, left_gap + right_gap)
            if max(prefix_max[i], suffix_max[i+1]) >= duration:
                max_gap = max(max_gap, left_gap + right_gap + duration)
        return max_gap