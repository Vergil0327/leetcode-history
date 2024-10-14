mod = 10**9 + 7

# bottom-up
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[0][0] = 1
for n in range(1, 1001):
    for x in range(1, n + 1):
        dp[n][x] = x * (dp[n - 1][x] + dp[n - 1][x - 1]) % mod

# top-down
@cache
def dfs(n, s):
    """
    distribute `n` performers to `s` non-empty stage => stirling number
    """
    if n < s: return 0 # 不可能將`n`表演者分配到全部舞台
    if s == 1: return 1
    # 1. distribute to current stage: s choices => s * dfs(n-1, s)
    # 2. distribute to current stage and exclude that stage: s choices => s * dfs(n-1, s-1)
    return (s * dfs(n - 1, s) + s * dfs(n - 1, s - 1)) % mod

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        res = 0
        for stage in range(1, min(n, x)+1):
            # there are `stage` stages containing 1 performers at least
            stage_scores = comb(x, stage) * pow(y, stage, mod)
            
            res += dfs(n, stage) * stage_scores
            
        return res%mod

    def numberOfWays(self, n: int, x: int, y: int) -> int:
        res = 0
        for stage in range(1, min(n, x)+1):
            # there are `stage` stages containing 1 performers at least
            stage_scores = comb(x, stage) * pow(y, stage, mod)
            res += dp[n][stage] * stage_scores
            
        return res%mod
