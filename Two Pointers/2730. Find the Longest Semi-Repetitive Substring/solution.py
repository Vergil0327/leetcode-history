# O(n)
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        pair = res = 0
        pairIdx = []
        l = r = 0
        while r < n:
            if r-1>=0 and s[r] == s[r-1]:
                pair += 1
                pairIdx.append(r)
            r += 1

            if l < r and pair > 1:
                l = pairIdx[-2]

            res = max(res, r-l)
        return res

# O(n^2)
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            pair = 0
            for j in range(i, n):
                if j > 0 and j-1 >= i and s[j] == s[j-1]:
                    pair += 1
                
                if pair > 1: break
                res = max(res, j-i+1)
        return res