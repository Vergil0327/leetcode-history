class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        def calLen(length):
            if length == 0: return 0
            elif length == 1: return 1
            elif length < 10: return 2
            elif length < 100: return 3
            else:
                return 4

        s = "#"+s
        dp = [[inf]*(k+1) for _ in range(n+1)]
        for kk in range(k+1):
            dp[0][kk] = 0

        for i in range(1, n+1):
            for kk in range(k+1):
                if kk > 0:
                    dp[i][kk] = dp[i-1][kk-1]

                removed = cnt = 0
                for j in range(i, 0, -1):
                    if s[j] == s[i]:
                        cnt += 1
                    else:
                        removed += 1
                        if removed > kk: break

                    dp[i][kk] = min(dp[i][kk], dp[j-1][kk-removed] + calLen(cnt))
        return dp[n][k]