class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        seen = {}
        for i, (l,r,w) in enumerate(intervals):
            if (l,r,w) not in seen:
                seen[l,r,w] = i
        intervals = sorted(seen) # list of tuples
        
        @cache
        def dfs(i, size):
            if size == 0 or i == len(intervals):
                return [0, []]
            
            skip = dfs(i + 1, size)

            j = bisect_right(intervals, (intervals[i][1]+1,))
            picked = dfs(j, size - 1)
            pick = [picked[0] + intervals[i][2], picked[1][:] + [seen[intervals[i]]]]
            pick[1].sort() # easy to find lexicographically smallest array

            if pick[0] > skip[0]:
                return pick
            elif pick[0] < skip[0]:
                return skip
            else: # find lexicographically smaller, i.e. after sorting
                return pick if pick[1] < skip[1] else skip

        return list(dfs(0, 4)[1])