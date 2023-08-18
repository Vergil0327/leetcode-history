class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[inf] * (target+1) for _ in range(n+1)] for _ in range(m)]
        
        for i in range(m):
            if houses[i] != 0:
                for prev in range(1, n+1):
                    for k in range(1, min(i+1, target)+1):
                        if houses[i] == prev:
                            dp[i][houses[i]][k] = min(dp[i][houses[i]][k], dp[i-1][prev][k] if i-1>=0 else 0)
                        else:
                            dp[i][houses[i]][k] = min(dp[i][houses[i]][k], dp[i-1][prev][k-1] if i-1>=0 else 0)

            else:
                for j in range(1, n+1):
                    for prev in range(1, n+1):
                        for k in range(1, min(i+1, target)+1):
                            if j == prev:
                                dp[i][j][k] = min(dp[i][j][k], (dp[i-1][prev][k] if i-1>=0 else 0) + cost[i][j-1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k],( dp[i-1][prev][k-1] if i-1>=0 else 0) + cost[i][j-1])

        res = inf
        for j in range(1, n+1):
            res = min(res, dp[m-1][j][target])
        return res if res != inf else -1
