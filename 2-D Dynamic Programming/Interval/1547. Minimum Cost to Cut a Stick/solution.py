class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @lru_cache(None)
        def dfs(i, j):
            start = bisect.bisect_right(cuts, i)
            end = bisect.bisect_left(cuts, j)
            if end-start < 1: return 0

            cost = j-i
            res = inf
            for k in range(start, end):
                mid = cuts[k]
                left, right = dfs(i, mid), dfs(mid, j)
                res = min(res, left+right+cost)

            return res
        return dfs(0, n)
    
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()

        m = len(cuts)

        dp = [[inf]*m for _ in range(m)]
        # length=1
        for i in range(m):
            dp[i][i] = 0

        # length=2
        for i in range(m-1):
            dp[i][i+1] = 0

        for length in range(3, m+1):
            for i in range(m-length+1):
                j = i+length-1
                cost = cuts[j]-cuts[i]
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+cost)
        return dp[0][m-1]