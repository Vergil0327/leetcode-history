class Solution:
    def countTexts(self, s: str) -> int:
        mod = 10**9+7

        # key: # of characters
        length = {"2":3, "3":3, "4":3, "5":3, "6":3, "7":4, "8":3, "9":4}
        n = len(s)

        s = "#" + s

        dp = [0]*(n+1)
        dp[0] = 1

        # 1-indexed
        for i in range(1, n+1):
            dp[i] += dp[i-1]

            if s[i] == s[i-1]:
                l = length.get(s[i], 0)
                for j in range(i-1, max(0, i-l), -1):
                    if s[i] == s[j]:
                        dp[i] += dp[j-1]
                    else:
                        break
            dp[i] %= mod

        return dp[n]
