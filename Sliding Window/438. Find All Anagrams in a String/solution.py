# https://labuladong.github.io/algo/1/12/
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = defaultdict(int)

        n = len(s)
        res = []
        valid = 0
        l = r = 0
        while r < n:
            ch = s[r]
            r += 1

            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    valid += 1
            
            # [l, r)
            while r-l >= len(p):
                if valid == len(need): res.append(l)

                ch = s[l]
                l += 1
                if ch in need:
                    if window[ch] == need[ch]:
                        valid -= 1
                    window[ch] -= 1
        return res