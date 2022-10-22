from collections import defaultdict

# https://labuladong.github.io/algo/1/12/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        window = defaultdict(lambda: 0)
        need = defaultdict(lambda: 0)
        for ch in s1:
            need[ch] += 1
            
        valid = 0
        l = 0
        for r in range(len(s2)):
            ch = s2[r]
            r += 1
                             
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    valid += 1

            while r-l >= len(s1):
                if valid == len(need): return True

                c = s2[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
            
        return False