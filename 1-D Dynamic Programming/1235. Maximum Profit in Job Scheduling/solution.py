
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

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # ? sort by starting point -> find minimum number of intervals to cover whole range
        # ? sort by ending point -> find maximum number of non-overlapping intervals 
        jobs = sorted([(start, end, p) for start, end, p in zip(startTime, endTime, profit)], key=lambda x:x[1])

        inf= float("inf")

        # we maintain an array which dp[t] is max profit untilt
        # we use 2-d array to store end time and max profit
        #  dp[t][0] : end time of current max profit
        #  dp[t][1] : maximum profit by the time t
        dp = [[0, 0]] # [endTime, current max profit until endTime]
        for job in jobs:
            start, end, profit = job[0], job[1], job[2]
            
            t = bisect.bisect_right(dp, [start, inf])-1 # find largest profit until `start`
            currMax = max(dp[-1][1], dp[t][1] + profit)
            dp.append([end, currMax])
            
        return dp[-1][1]

# we maintain a dp[t] array which stores pair [end time, max profit until end time] at current t
class SolutionTLE:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(end, start, p) for start, end, p in zip(startTime, endTime, profit)])
        
        n = len(jobs)
        dp = [[0, 0]]
        
        for job in jobs:
            end, start, p = job[0], job[1], job[2]
            
            # dp[t] = max(dp[t-1], dp[j] + profit) where j <= current start time when end time is t
            # find max profit before current end time
            # can be previous non-overlapping job + current profit: dp[j] + p
            # or max profit before current: dp[t-1]
            currMax = dp[-1][1]
            for j in range(len(dp)):
                if dp[j][0] <= start:
                    currMax = max(currMax, dp[j][1] + p)
            dp.append([end, currMax])

        return dp[-1][1]