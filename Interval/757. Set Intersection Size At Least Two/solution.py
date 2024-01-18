class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        n = len(intervals)

        overlapping_groups = [] # [containing_size, overlap1, overlap2] where overlap1 < overlap2
        for i in range(n):
            if not overlapping_groups or overlapping_groups[-1][2] < intervals[i][0]:
                overlapping_groups.append([2, intervals[i][1]-1, intervals[i][1]])
            else:
                size, overlap1, overlap2 = overlapping_groups[-1]
                start, end = intervals[i]
                if start <= overlap1: continue
                
                if end == overlap2:
                    overlapping_groups[-1] = [size+1, end-1, end]
                else:
                    overlapping_groups[-1] = [size+1, overlap2, end]

        return sum(group[0] for group in overlapping_groups)