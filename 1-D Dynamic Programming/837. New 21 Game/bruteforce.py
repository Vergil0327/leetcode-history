# TLE
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0: return 1

        def dfs(score):
            if score >= k: return 1 if score <= n else 0

            prob = 0
            for pt in range(1, maxPts+1):
                prob += dfs(score+pt) * 1/maxPts
            return prob
        return dfs(0)

# TLE
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0: return 1

        mx_score = k-1 + maxPts
        
        dp = [0]* (mx_score+1)
        dp[0] = 1

        for sc in range(1, mx_score+1):
            for pt in range(1, maxPts+1):
                if sc-pt >= 0 and sc-pt < k:
                    dp[sc] += dp[sc-pt] * 1/maxPts

        prob = 0
        for sc in range(k, n+1):
            prob += dp[sc]
        return prob