class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        n, m = len(target), len(words[0])

        target = "#" + target
        dictionary = [defaultdict(int) for _ in range(m+1)]
        for word in words:
            for i, ch in enumerate(word):
                dictionary[i+1][ch] += 1
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        # dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 1

        for i in range(1, n+1):
            ch = target[i]

            for j in range(1, m+1):
                # use j-th column of each word + not use j-th column of each word
                dp[i][j] += dp[i-1][j-1] * dictionary[j][ch] + dp[i][j-1]
                dp[i][j] %= mod

        return dp[n][m]

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1_000_000_007
        n = len(target)
        m = len(words[0])
        dictionary = [defaultdict(int) for _ in range(m)]
        for word in words:
            for i, ch in enumerate(word):
                dictionary[i][ch] += 1

        @lru_cache(None)
        def dfs(i, j):
            if i == n: return 1
            if j == m: return 0

            res = dfs(i, j+1)%MOD
            if target[i] in dictionary[j]:
                res += dfs(i+1, j+1) * dictionary[j][target[i]]
            return res % MOD

        return dfs(0, 0)
