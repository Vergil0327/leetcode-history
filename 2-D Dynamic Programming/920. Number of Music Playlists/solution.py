class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = int(1e9+7)

        # dfs[i][j] be the number of playlists of length i that have exactly j unique songs
        @lru_cache(None)
        def dfs(i, j):
            if i == goal:
                # since goal >= n > k, if we have `goal` songs in playlist
                # we've must have n song in playlist and got `goal-n` duplicate song
                if j == n: return 1
                return 0

            res = dfs(i+1, j) * (j-k) if j-k > 0 else 0
            res += dfs(i+1, j+1) * (n-j)
            return res % MOD
        return dfs(0, 0)

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = int(1e9+7)

        # dfs[i][j] be the number of playlists of length i that have exactly j unique songs
        dp = [[0] * (n+1) for _ in range(goal+1)]
        dp[0][0] = 1

        for i in range(1, goal+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j-1] * (n-j+1) # first time choose j song. +1 for 1-based shift
                dp[i][j] += dp[i-1][j] * max(j-k, 0) # duplicate song
                dp[i][j] %= MOD

        return dp[goal][n]