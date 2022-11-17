
# Top-Down + Memorization + Binary Search
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time = sorted([(start, end, p) for start, end, p in zip(startTime, endTime, profit)])
        inf= float("inf")
        n = len(time)
        
        def bisect_right(i):
            l, r = i+1, n
            while l < r:
                mid = l + (r-l)//2
                if time[mid][0] < time[i][1]:
                    l = mid+1
                else:
                    r = mid
            return l
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            profit = dfs(i+1)
            j = bisect_right(i)
            profit = max(profit, dfs(j) + time[i][2])
            
            return profit
        
        return dfs(0)