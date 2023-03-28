class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = int(1e9+7)

        n = len(types)

        # dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        types = [[-1, -1]] + types
        for i in range(1, n+1):
            count, mark = types[i][0], types[i][1]
            for j in range(target+1):
                for cnt in range(count+1):
                    dp[i][j] += dp[i-1][j-cnt*mark] if j-cnt*mark>=0 else 0
                    dp[i][j] %= MOD

        return dp[n][target]
    
# efficiency optimization
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = int(1e9+7)

        n = len(types)

        # dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        types = [[-1, -1]] + types
        for i in range(1, n+1):
            count, mark = types[i][0], types[i][1]
            for j in range(target+1):
                for cnt in range(min(j//mark, count)+1):
                    dp[i][j] += dp[i-1][j-cnt*mark]
                    dp[i][j] %= MOD

        return dp[n][target]
    
# Space Optimization

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = int(1e9+7)

        n = len(types)

        # dp[i][j]: the number of ways you can earn exactly j points in the exam considering types[:i]
        # dp = [[0]*(target+1) for _ in range(n+1)]
        # dp[0][0] = 1
        dp = [0]*(target+1)
        dp[0] = 1

        types = [[-1, -1]] + types
        for i in range(1, n+1):
            count, mark = types[i][0], types[i][1]
            for j in range(target, -1, -1):
                for cnt in range(1, min(j//mark, count)+1):
                    dp[j] += dp[j-cnt*mark]
                    dp[j] %= MOD

        return dp[target]