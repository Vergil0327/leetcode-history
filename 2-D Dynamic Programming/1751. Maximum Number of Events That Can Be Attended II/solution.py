class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda evt:(evt[1],evt[0]))
        n = len(events)
        events = [[-inf,-inf,0]] + events
        endTime = [evt[1] for evt in events]

        dp = [[-inf]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, min(i, k)+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                idx = bisect.bisect_left(endTime, events[i][0])-1 # since endtime inclusive -= 1 position
                dp[i][j] = max(dp[i][j], dp[idx][j-1] + events[i][2])
                
        return max(dp[n])
