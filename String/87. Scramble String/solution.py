class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        
        # Boost Performance, if characters are not matched, it can't be True
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


class SolutionBruteForce:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        
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
