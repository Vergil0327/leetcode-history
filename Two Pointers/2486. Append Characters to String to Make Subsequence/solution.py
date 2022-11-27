class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not (set(s) & set(t)): return len(t) # can omit this line
        
        l, r = 0, 0
        while l < len(s):
            if s[l] == t[r]:
                r += 1
                if r == len(t): return 0
            l += 1
        return len(t) - r