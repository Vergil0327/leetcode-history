# just simulate process
class Solution:
    def minimumSteps(self, s: str) -> int:
        l, r = 0, len(s)-1
        res = 0
        while l < r:
            while l < r and s[l] == "0":
                l += 1
            while l < r and s[r] == "1":
                r -= 1
            if l >= r: break

            res += r-l
            l, r = l+1, r-1
        return res
    
# Optimized
class Solution:
    def minimumSteps(self, s: str) -> int:
        res = black = 0
        
        for c in s:
            if c == '0':
                res += black
            else:
                black += 1
        
        return res