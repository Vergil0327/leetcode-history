class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        s = "#" + s
        dp = [inf]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            count = Counter()
            occur = Counter()
            for j in range(i, 0, -1):
                if count[s[j]] > 0:
                    occur[count[s[j]]] -= 1
                    if occur[count[s[j]]] == 0:
                        del occur[count[s[j]]]
                count[s[j]] += 1
                occur[count[s[j]]] += 1

                if len(occur) == 1: # balanced
                    dp[i] = min(dp[i], dp[j-1]+1)
        return dp[n]
