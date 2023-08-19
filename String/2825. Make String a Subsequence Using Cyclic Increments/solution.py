class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        s = ""
        for ch in str1:
            s += chr((ord(ch)-ord("a")+1)%26 + ord("a"))

        i = 0
        for ch1, ch2 in zip(str1, s):
            if ch1 == str2[i] or ch2 == str2[i]:
                i += 1
            if i == len(str2): return True
        return i == len(str2)