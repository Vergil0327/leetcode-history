mod = 10**9 + 7
class Solution:
    def countWinningSequences(self, s: str) -> int:
        memo = [[defaultdict(lambda: -1) for _ in range(4)] for _ in range(len(s))]
        ch2idx = {
            "": 0,
            "F": 1,
            "E": 2,
            "W": 3,
        }

        def dfs(i, prev, diff):
            if i == len(s): return int(diff > 0)

            if memo[i][ch2idx[prev]][diff] != -1: return memo[i][ch2idx[prev]][diff]

            res = 0
            if s[i] == "F":
                if prev != "F":
                    res += dfs(i+1, "F", diff)
                if prev != "E":
                    res += dfs(i+1, "E", diff - 1)
                if prev != "W":
                    res += dfs(i+1, "W", diff + 1)
            elif s[i] == "W":
                if prev != "F":
                    res += dfs(i+1, "F", diff - 1)
                if prev != "E":
                    res += dfs(i+1, "E", diff + 1)
                if prev != "W":
                    res += dfs(i+1, "W", diff)
            else: # s[i] == "E"
                if prev != "F":
                    res += dfs(i+1, "F", diff + 1)
                if prev != "E":
                    res += dfs(i+1, "E", diff)
                if prev != "W":
                    res += dfs(i+1, "W", diff - 1)
            res %= mod
            memo[i][ch2idx[prev]][diff] = res
            return res
        return dfs(0, "", 0)
    

# bottom-up: by @lee215
class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        s = ['FWE'.find(c) for c in s]
        dp = [[Counter() for j in range(3)] for i in range(n)]

        for i in range(n):
            for j in range(3):
                d = (j - s[i] + 1) % 3 - 1
                if i == 0:
                    dp[i][j][d] = 1
                else:
                    for j2 in range(3):
                        if j != j2:
                            for v in dp[i - 1][j2]:
                                dp[i][j][v + d] += dp[i - 1][j2][v]
                                dp[i][j][v + d] %= mod
        res = 0
        for j in range(3):
            for v in range(1, n + 1):
                res += dp[n - 1][j][v]
        return res % mod