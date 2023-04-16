# top-down
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1_000_000_007
        n = len(target)
        m = len(words[0])
        dictionary = [defaultdict(int) for _ in range(m)]

        for i in range(len(words)):
            for j in range(m):
                dictionary[j][words[i][j]] += 1
        
        @lru_cache(None)
        def dfs(i, j):
            if i == n: return 1
            if j == m: return 0

            res = dfs(i, j+1)%MOD
            if target[i] in dictionary[j]:
                res += dfs(i+1, j+1) * dictionary[j][target[i]]
            return res % MOD

        return dfs(0, 0)

# bottom-up
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1_000_000_007
        n = len(target)
        target = "#" + target

        m = len(words[0])

        count = [defaultdict(int) for _ in range(m+1)]
        for i in range(len(words)):
            for j in range(1, m+1):
                count[j][words[i][j-1]] += 1
        
        dp = [[0]* (m+1) for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] += dp[i][j-1]
                if target[i] in count[j]:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1] * count[j][target[i]]) % MOD
                
        return dp[n][m]