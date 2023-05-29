class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        binK = bin(k)[2:]

        maxLen = n = len(s)
        for i in range(n):
            if s[i] == "1":
                if n-i > len(binK) or (n-i == len(binK) and int(s[i:]) > int(binK)):
                    maxLen -= 1
                else:
                    return maxLen
            
        return maxLen
