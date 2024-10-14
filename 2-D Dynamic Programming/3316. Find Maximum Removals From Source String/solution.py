class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        s = ""
        j = 0
        for i, ch in enumerate(source):
            if j < len(targetIndices) and i == targetIndices[j]:
                s += "#"
                j += 1
            else:
                s += ch

        @cache
        def dfs(i, j):
            if j >= len(pattern): return 0
            if i >= len(s): return inf
            
            res = dfs(i+1, j + (1 if j < len(pattern) and s[i] == pattern[j] else 0))

            if s[i] == "#":
                res = min(res, dfs(i+1, j + (1 if j < len(pattern) and source[i] == pattern[j] else 0)) + 1)
            return res
        
        return len(targetIndices) - dfs(0, 0)
    

class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        s = set(targetIndices)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == m:
                return 0 if j == n else -float("inf")

            if j == n:
                return int(i in s) + dfs(i + 1, j)

            res = int(i in s) + dfs(i + 1, j)
            if source[i] == pattern[j]:
                res = max(res, dfs(i + 1, j + 1))
            return res
        res = dfs(0, 0)
        return res if res != -float("inf") else 0

    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        s = set(targetIndices)
        dp = [[-float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n, -1, -1):
                if j == n:
                    dp[i][j] = int(i in s) + dp[i + 1][j]
                else:
                    dp[i][j] = int(i in s) + dp[i + 1][j]
                    if source[i] == pattern[j]:
                        dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
        return dp[0][0] if dp[0][0] != -float("inf") else 0