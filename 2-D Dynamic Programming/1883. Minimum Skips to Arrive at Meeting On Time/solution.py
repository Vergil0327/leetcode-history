# TLE at final testcase
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist)/speed > hoursBefore: return -1

        eps = 1e-8
        n = len(dist)
        dist = [0] + dist
        def computeTime(skips):
            dp = [[1e20] * (skips+1) for _ in range(n+1)]
            dp[0][0] = 0
            for i in range(1, n+1):
                rest = ceil(dp[i-1][0] + dist[i]/speed - eps)
                dp[i][0] = min(dp[i][0], rest)

            for i in range(1, n+1):
                for j in range(1, skips+1):
                    if i == n:
                        dp[i][j] = dp[i-1][j] + dist[i]/speed
                    else:
                        skip_rest = dp[i-1][j-1] + dist[i]/speed
                        rest = ceil(dp[i-1][j] + dist[i]/speed - eps)
                        dp[i][j] = min(skip_rest, rest)
            return dp[n][skips]

        l = 0
        r = n
        while l < r:
            mid = l + (r-l)//2 # skip times
            timeNeeded = computeTime(mid)
            if timeNeeded > hoursBefore:
                l = mid+1
            else:
                r = mid

        return l

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        epsilon = 1e-8
        n = len(dist)
        dist = [0] + dist

        dp = [[1e20] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        for i in range(1, n+1):
            for j in range(i+1):
                if i == n:
                    dp[i][j] = dp[i-1][j] + dist[i]/speed
                else:
                    rest = ceil(dp[i-1][j] + dist[i]/speed-epsilon)
                    dp[i][j] = rest
                    if j-1 >= 0:
                        skip_rest = dp[i-1][j-1] + dist[i]/speed
                        dp[i][j] = min(dp[i][j], skip_rest)
        
        for j in range(n):
            if dp[n][j] <= hoursBefore: return j
        return -1

class Solution_TLE:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist)/speed > hoursBefore: return -1

        n = len(dist)
        @lru_cache(None)
        def dfs(i, prev):
            if i == n:
                return 1 if prev <= hoursBefore else inf

            # skip rest
            a = dfs(i+1, (prev + dist[i]/speed)%1) + 1

            # rest
            b = dfs(i+1, 0)

            return min(a, b)
        return dfs(0, 0)-1 # don't need to rest at last time