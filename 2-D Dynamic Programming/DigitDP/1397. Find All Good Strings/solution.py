class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10**9 + 7

        def kmp_preprocess(s):
            n = len(s)
            lps = [0]*n

            for i in range(1, n):
                j = lps[i-1]
                while j >= 1 and s[i]!=s[j]:
                    j = lps[j-1]
                lps[i] = j + int(s[i] == s[j])
            return lps

        lps = kmp_preprocess(evil)

        @cache
        def dfs(i, j, lowerbound, upperbound):
            if j == len(evil): return 0
            if i == n: return 1

            start = ord(s1[i]) if lowerbound else ord("a")
            end = ord(s2[i]) if upperbound else ord("z")
            res = 0
            for k in range(start, end+1):
                ch = chr(k)

                # find longest prefix suffix from kmp algo.
                jj = j
                while jj > 0 and evil[jj] != ch:
                    jj = lps[jj-1]
                jj += int(evil[jj] == ch)

                res += dfs(i+1, jj, lowerbound and ch == s1[i],  upperbound and ch == s2[i])
                res %= mod

            return res
        return dfs(0, 0, True, True)
