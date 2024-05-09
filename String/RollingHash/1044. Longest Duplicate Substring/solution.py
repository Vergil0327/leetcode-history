class Solution:
    def longestDupSubstring(self, s: str) -> str:
        len2start = {}

        n = len(s)
        base = 31
        mod = 10**11 + 7
        nums = [ord(ch)-ord("a") for ch in s]
        
        # RABIN-KARP, Rolling Hash
        # sliding window, [i-len+1, i]
        def check_rolling_hash(s: str, length: int) -> bool:
            
            visited = set()
            rolling_hash = 0
            pow_base_len = pow(base, length, mod)
            for i in range(n):
                rolling_hash = rolling_hash*base + nums[i]
                if i >= length:
                    rolling_hash -= pow_base_len*nums[i-length]
                rolling_hash = (rolling_hash+mod) % mod
                
                if i-length+1 >= 0:
                    if rolling_hash in visited:
                        len2start[length] = i-length+1
                        return True
                    visited.add(rolling_hash)
            return False
        
        # binary search length of duplicate substring
        l, r = 0, n-1
        while l < r:
            mid = r - (r-l)//2
            if check_rolling_hash(s, mid):
                l = mid
            else:
                r = mid-1
        
        return s[len2start[l]:len2start[l]+l] if l > 0 else ""