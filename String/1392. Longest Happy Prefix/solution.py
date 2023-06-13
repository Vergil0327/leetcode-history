class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        
        P, PP = 33, 1 # P for prefix, PP for suffix
        mod = 10**9 + 7
        i, j = 0, n-1
        maxLen = 0
        hashedPrefix = hashedSuffix = 0
        for k in range(n-1):
            hashedPrefix = hashedPrefix * P + ord(s[i])
            hashedPrefix %= mod
            
            # hashedSuffix = ord(s[j]) * pow(P, k, mod) + hashedSuffix
            hashedSuffix = ord(s[j]) * PP + hashedSuffix
            
            PP = PP * P % mod
            hashedSuffix %= mod

            if hashedPrefix == hashedSuffix:
                if s[:k+1] == s[-(k+1):]:
                    maxLen = k+1
            i, j = i+1, j-1
            
        return s[:maxLen]