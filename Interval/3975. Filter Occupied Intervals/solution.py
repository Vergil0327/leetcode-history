class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        if not occupiedIntervals:
            return []
    
        intervals = sorted(occupiedIntervals, key=lambda x: x[0])
        
        merged = [intervals[0][:]]
        for l, r in intervals[1:]:
            if l <= merged[-1][1] + 1:
                merged[-1][1] = max(merged[-1][1], r)
            else:
                merged.append([l, r])
        
        result = []
        for l, r in merged:
            if r < freeStart or l > freeEnd:
                result.append([l, r])
            else:
                if l < freeStart:
                    result.append([l, freeStart - 1])
                if r > freeEnd:
                    result.append([freeEnd + 1, r])
        
        return result
            