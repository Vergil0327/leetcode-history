class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        a = e = i = o = u = 0

        n = len(s)
        vowels = {(0,0,0,0,0): -1}
        res = 0
        for j in range(n):
            if s[j] == "a":
                a += 1
                a %= 2
            elif s[j] == "e":
                e += 1
                e %= 2
            elif s[j] == "i":
                i += 1
                i %= 2
            elif s[j] == "o":
                o += 1
                o %= 2
            elif s[j] == "u":
                u += 1
                u %= 2

            key = (a,e,i,o,u)
            if key in vowels:
                res = max(res, j-vowels[key])
            else:
                vowels[key] = j
        return res
