class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        n = len(sentence)
        def cost(s):
            return (k-len(s)) ** 2

        dp = [float("inf")] * (n+1)
        dp[0] = 0

        sentence = " " + sentence
        for i in range(1, n+1):
            if sentence[i] == " ":
                for j in range(i-1, max(i-k-2, -1), -1):
                    if sentence[j] == " ":
                        dp[i] = min(dp[i], dp[j] + cost(sentence[j+1:i]))
        for i in range(n, -1, -1):
            if sentence[i] == " ":
                return dp[i]
        

class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        @cache
        def dfs(i):
            if s[-1] - s[i] + n - i - 1 <= k:
                return 0
            ans, j = inf, i + 1
            # j - i - 1: white spaces
            while j < n and (t := s[j] - s[i] + j - i - 1) <= k:
                ans = min(ans, (k - t) ** 2 + dfs(j))
                j += 1
            return ans

        t = [len(w) for w in sentence.split()]
        n = len(t)
        s = list(accumulate(t, initial=0))
        return dfs(0)