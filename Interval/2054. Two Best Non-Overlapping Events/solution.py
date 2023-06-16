class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        suffixMax = []
        prefixMax = []
        for i in range(n):
            suffixMax.append([events[i][0], events[i][2]])
            prefixMax.append([events[i][1], events[i][2]])
        
        suffixMax.sort()
        suffixMax = suffixMax + [[inf,0]] # [start_time, max_value_until]
        for i in range(n-1, -1, -1):
            suffixMax[i][1] = max(suffixMax[i][1], suffixMax[i+1][1])

        prefixMax.sort()
        prefixMax = [[-inf,0]] + prefixMax # [end_time, max_value_until]
        for i in range(1, n+1):
            prefixMax[i][1] = max(prefixMax[i-1][1], prefixMax[i][1])
        
        res = 0
        for i in range(n):            
            # search > end_time max from [k, n-1]
            l, r = 0, n
            while l < r:
                mid = l + (r-l)//2
                if suffixMax[mid][0] <= events[i][1]:
                    l = mid+1
                else:
                    r = mid

            res = max(res, events[i][2] + suffixMax[l][1])
        
            # search < start_time max from [0,j]
            l, r = 0, n
            while l < r:
                mid = r - (r-l)//2
                if prefixMax[mid][0] >= events[i][0]:
                    r = mid-1
                else:
                    l = mid
            res = max(res, events[i][2] + prefixMax[l][1])

        return res
    
# Optimized
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        res = max_val_until = 0
        minHeap = [] # (end_time, val)
        for start, end, value in sorted(events):
            while minHeap and minHeap[0][0] < start:
                _, val = heapq.heappop(minHeap)
                max_val_until = max(max_val_until, val)

            res = max(res, value + max_val_until)
            heapq.heappush(minHeap, [end, value])

        return res