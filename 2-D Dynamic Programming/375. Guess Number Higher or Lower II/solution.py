# Top-Down
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l >= r: return 0

            res = inf
            for i in range(l, r+1):
                res = min(res, max(dfs(l, i-1), dfs(i+1, r)) + i)
            return res
        return dfs(1, n)

# Bottom-Up
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j]: the minimum amount of money you need to guarantee a win regardless of what number I pick for n from i to j
        dp = [[0] * (n+2) for _ in range(n+2)] # n+2才不會讓dp[k+1]越界
        
        # length 從2開始是因為，當區間只有1時不用猜，答案一定是該數
        for length in range(2, n+1):
            for i in range(1, n-length+1+1): # j = i+length-1 <= n
                j = i+length-1

                dp[i][j] = inf
                for k in range(i, j+1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))

        return dp[1][n]
