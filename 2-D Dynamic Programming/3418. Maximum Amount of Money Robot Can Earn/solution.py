class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])

        memo = [[[-inf, -inf, -inf] for _ in range(n)] for _ in range(m)]
        # dfs(r,c,x): the maximum amount at (r,c) and already nertralized x times
        def dfs(r, c, x):
            if r < 0 or r >= m or c < 0 or c >= n: return -inf
            if r == m-1 and c == n-1:
                if x < 2 and coins[r][c] < 0: return 0 # neutralize

                return coins[r][c]
            if memo[r][c][x] > -inf: return memo[r][c][x]

            # don't nertralize
            memo[r][c][x] = dfs(r+1, c, x) + coins[r][c]
            memo[r][c][x] = max(memo[r][c][x], dfs(r, c+1, x) + coins[r][c])
            
            # neutralize
            if coins[r][c] < 0 and x < 2:
                memo[r][c][x] = max(memo[r][c][x], dfs(r+1, c, x+1))
                memo[r][c][x] = max(memo[r][c][x], dfs(r, c+1, x+1))
            return memo[r][c][x]
        
        return dfs(0, 0, 0)