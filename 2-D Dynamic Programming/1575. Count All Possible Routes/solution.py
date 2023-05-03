class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        n = len(locations)

        @cache
        def dfs(cur, f):
            res = 1 if cur == finish else 0
            
            for nxt in range(n):
                if nxt == cur: continue

                cost = abs(locations[nxt]-locations[cur])
                if (remain := f-cost) >= 0:
                    res = (res + dfs(nxt, remain))%mod
            return res

        return dfs(start, fuel)

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        n = len(locations)

        dp = [[0]*(fuel+1) for _ in range(n)]
        dp[start][fuel] = 1

        for f in range(fuel, -1, -1):
            for i in range(n):
                for j in range(n):
                    if i == j: continue
                    
                    cost = abs(locations[i] - locations[j])
                    if f+cost <= fuel:
                        dp[i][f] += dp[j][f+cost]
                        dp[i][f] %= mod

        res = 0
        for f in range(fuel+1):
            res = (res + dp[finish][f])%mod
        return res
    
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9+7
        n = len(locations)
        startPos = locations[start]
        finishPos = locations[finish]
        locations.sort()

        startIdx = endIdx = -1
        for i in range(n):
            if locations[i] == startPos:
                startIdx = i
            if locations[i] == finishPos:
                endIdx = i

        dp = [[[0]*3 for _ in range(n)]for _ in range(fuel+1)]
        dp[fuel][startIdx][0] = 1

        for f in range(fuel, -1, -1):
            for city in range(n):
                # dp[f][city][state], state=0 -> stay at city; state=1 -> moving right; state=2 -> moving left
                if city > 0 and f+(cost := abs(locations[city] - locations[city-1])) <= fuel:
                    dp[f][city][0] += dp[f+cost][city-1][1] + dp[f+cost][city-1][0]
                    dp[f][city][0] %= mod
                    dp[f][city][1] += dp[f+cost][city-1][1] + dp[f+cost][city-1][0]
                    dp[f][city][1] %= mod
                if city < n-1 and f+(cost := abs(locations[city] - locations[city+1])) <= fuel:
                    dp[f][city][0] += dp[f+cost][city+1][2] + dp[f+cost][city+1][0]
                    dp[f][city][0] %= mod
                    dp[f][city][2] += dp[f+cost][city+1][2] + dp[f+cost][city+1][0]
                    dp[f][city][2] %= mod
        
        res = 0
        for f in range(fuel+1):
            res = (res + dp[f][endIdx][0])%mod
        
        return res