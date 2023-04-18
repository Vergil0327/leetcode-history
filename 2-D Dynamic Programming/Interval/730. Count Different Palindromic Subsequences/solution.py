class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9+7

        @cache
        def dfs(l, r):
            if l > r: return 0
            if l == r: return 1

            res = 0
            for ch in "abcd":
                i, j = l, r
                while i <= r and s[i] != ch:
                    i += 1
                while j >= l and s[j] != ch:
                    j -= 1
                if i == j:
                    res += 1
                elif i < j:
                    res += dfs(i+1, j-1) + 2
            return res%MOD
        return dfs(0, len(s)-1)