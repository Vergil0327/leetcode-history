class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        minCost = [inf]*n
        for i in range(n):
            for j in range(m):
                minCost[i] = min(minCost[i], cost[j][i])
        @cache
        def dfs(i, state):
            if i == m:
                return sum(minCost[j] for j in range(n) if (state>>j)&1 == 0)

            res = inf
            for j in range(n):
                res = min(res, dfs(i+1, state | (1<<j)) + cost[i][j]) 
            return res

        return dfs(0, 0)

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        cost = [[0]*m] + cost

        dp = [[inf]*(1<<n) for _ in range(m+1)]
        dp[0][0] = 0

        cost2 = [[0]*(1<<n) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for state in range(1<<n):
                cost2[i][state] = sum(cost[i][j] for j in range(n) if (state>>j)&1)

        for i in range(1, m+1):
            for state in range(1<<n):
                substate = state
                while substate > 0:
                    dp[i][state] = min(dp[i][state], dp[i-1][state-substate] + cost2[i][substate])
                    substate = (substate-1)&state

                minPath = min(cost[i][j] for j in range(n))
                dp[i][state] = min(dp[i][state], dp[i-1][state] + minPath)
        return dp[m][(1<<n)-1]