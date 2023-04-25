class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = [[-inf]*n for _ in range(n)]
        presum = [0] + list(accumulate(stones))
        
        @lru_cache(None)
        def dfs(l, r):
            if l > r: return 0
            if memo[l][r] != -inf: return memo[l][r]

            # alice = (presum[r+1]-presum[l+1]) - dfs(l+1, r)
            memo[l][r] = (presum[r+1]-presum[l+1]) - dfs(l+1, r)
            # alice = max(alice, presum[r]-presum[l] - dfs(l, r-1))
            memo[l][r] = max(memo[l][r], presum[r]-presum[l] - dfs(l, r-1))

            return memo[l][r]
        return dfs(0, len(stones)-1)

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # presum = [0]*(n+1)
        # for i in range(1, n+1):
        #     presum[i] = presum[i-1] + stones[i-1]
        presum = [0] + list(accumulate(stones))

        # dp[i][j]: the maximum difference when playing in stones[i:j]
        dp = [[-inf]*n for _ in range(n)]

        # n starts from 2 to 1000 at most
        # length = 2
        for i in range(n-1):
            dp[i][i+1] = max(stones[i], stones[i+1])

        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                # remove i (leftmost)
                dp[i][j] = presum[j+1]-presum[i+1] - dp[i+1][j]
                
                # remove j (rightmost)
                dp[i][j] = max(dp[i][j], presum[j]-presum[i] - dp[i][j-1])
        return dp[0][n-1]
