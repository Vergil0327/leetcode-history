class Solution:
    def longestDupSubstring(self, s: str) -> str:
        len2start = {}

        # RABIN-KARP, Rolling Hash
        def checkOK(s: str, length: int) -> bool:
            BASE = 26
            MOD = 1e7+7
            L = length
            SHIFFT = ord("a")
            rollingHash = 0
            visited = set()

            POWER_BASE_LEN = 1 # BASE ** (L-1)
            for i in range(1, L):
                POWER_BASE_LEN = POWER_BASE_LEN * BASE % MOD
            
            # sliding window, [i-len, i]
            for i in range(L):
                num = ord(s[i])-SHIFFT
                # baba b
                if i >= L:
                    rollingHash = (rollingHash - (ord(s[r-L])-SHIFFT) * POWER_BASE_LEN % MOD + MOD)%MOD
                rollingHash = rollingHash * BASE + num

                if i-L-1 >=0:
                    if rollingHash in visited:
                        len2start[length] = i-L-1
                        return True
                    visited.add(rollingHash)
            return False

        # binary search length of duplicate substring
        l, r = 1, len(s)-1
        while l < r:
            mid = r - (r-l)//2
            if checkOK(s, mid):
                l = mid
            else:
                r = mid-1
        
        if checkOK(s, l):
            return s[len2start[l], l]
        else:
            return ""