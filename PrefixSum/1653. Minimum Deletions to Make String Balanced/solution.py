class Solution:
    def minimumDeletions(self, s: str) -> int:
        # dp[i][0] ending at a
        # dp[i][1] ending at b
        n = len(s)
        dp = [[inf, inf] for _ in range(n+1)]
        dp[0][0] = dp[0][1] = 0

        s = "#" + s
        for i in range(1, n+1):
            if s[i] == "a":
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
        return min(dp[n])

# 3-pass
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        presum = [0] * n
        presum[0] = 1 if s[0] == "b" else 0
        for i in range(1, n):
            presum[i] = presum[i-1] + (1 if s[i] == "b" else 0)

        sufsum = [0] * n
        sufsum[-1] = 1 if s[-1] == "a" else 0
        for i in range(n-2, -1, -1):
            sufsum[i] = sufsum[i+1] + (1 if s[i] == "a" else 0)

        res = min(presum[n-1], sufsum[0]) # min(全變成a, 全變成b)
        for i in range(n-1):
            res = min(res, presum[i] + sufsum[i+1]) # [0:i]都變成a, [i+1:]都變成b
        return res