# daily challenge 2023/03/30
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        @lru_cache(None)
        def dfs(l, r, m, n):
            if s1[l:r+1] == s2[m:n+1]: return True
            if l > r or m > n: return False
            
            for i in range(l+1, r+1):
                # x = s[l:i]
                # y = s[i:r+1]
                lenx = i-l
                leny = r+1-i
                
                if dfs(l, i-1, m, m+lenx-1) and dfs(i, r, m+lenx, n): return True
                if dfs(i, r, m, m+leny-1) and dfs(l, i-1, m+leny, n): return True
            return False
        return dfs(0, n-1, 0, n-1)

# brute force
class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        
        # Boost Performance, if characters doesn't match, it can't be True
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            s1a, s1b = s1[:i], s1[i:]
            for j in range(1, n):
                s2a, s2b = s2[:j], s2[j:]
                if len(s1a) == len(s2a) and len(s1b) == len(s2b):
                    if self.isScramble(s1a, s2a) and self.isScramble(s1b, s2b):
                        return True
                if len(s1a) == len(s2b) and len(s1b) == len(s2a):
                    if self.isScramble(s1a, s2b) and self.isScramble(s1b, s2a):
                        return True
        return False
