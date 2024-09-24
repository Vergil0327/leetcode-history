class Solution:
    """
    top-down dp: pick or skip strategy
    """
    def maxScore(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)

        dp = [[-1]*m for _ in range(n)]
        def dfs(i, j):
            if j >= m: return 0
            if i >= n: return -inf

            if dp[i][j] == -1:
                dp[i][j] = max(dfs(i+1, j), dfs(i+1, j+1) + a[j] * b[i])
            return dp[i][j]

        return dfs(0, 0)

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        dp = [-inf]*4
        for num in b:
            dp[3] = max(dp[3], dp[2] + a[3] * num)
            dp[2] = max(dp[2], dp[1] + a[2] * num)
            dp[1] = max(dp[1], dp[0] + a[1] * num)
            dp[0] = max(dp[0], a[0] * num)
        return dp[3]