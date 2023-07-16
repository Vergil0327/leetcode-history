class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbid = set()
        maxLen = 0
        for s in forbidden:
            forbid.add(s)
            maxLen = max(maxLen, len(s))

        n = len(word)
        res = l = r = 0
        while r < n:
            r += 1
            for left in range(r-1, max(l, r-maxLen)-1, -1):
                if word[left:r] in forbid:
                    l = left+1
                    break
            res = max(res, r-l)
        return res

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        seen = set(forbidden)
        n = len(word)

        res = 0
        dp = [n] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1]
            for j in range(i, min(dp[i], n, i+10)):
                if word[i:j+1] in seen:
                    dp[i] = j
                    break
            res = max(res, dp[i]-i)
        return res