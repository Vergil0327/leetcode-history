class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)
        def dfs(i, paid_time):
            if i+paid_time >= n:
                return 0
            if i == n: # pain all ther wall
                return 0 if paid_time >= 0 else inf

            res = dfs(i+1, paid_time+time[i]) + cost[i]
            res = min(res, dfs(i+1, paid_time-1))
            
            return res
        return dfs(0, 0)
    

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        dp = [[inf]*(n+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0

        for i, (c, t) in enumerate(zip(cost, time)):
            for wall in range(1, n+1):
                dp[i][wall] = min(dp[i-1][wall], dp[i-1][max(0, wall-t-1)]+c)
        return dp[n-1][n]