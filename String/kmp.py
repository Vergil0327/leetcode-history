def preprocess(s):
    n = len(s)
    lps = [0]*n

    for i in range(1, n):
        j = lps[i-1]
        while j >= 1 and s[i]!=s[j]:
            j = lps[j-1]
        lps[i] = j + int(s[i] == s[j])
    return lps

# return index of target in s
def kmp(s: str, target: str):
    n = len(s)
    m = len(target)
    if m == 0: return 0
    if n == 0: return -1

    # preprocess
    # longest prefix suffix
    lps = preprocess(target)

    # find target word in s
    dp = [0]*n
    dp[0] = int(s[0] == target[0])
    if len(target) == 1 and dp[0] == 1: return 0

    for i in range(1, n):
        j = dp[i-1]
        while j > 0 and s[i] != target[j]:
            j = lps[j-1]
        dp[i] = j + (s[i] == target[j])
        if dp[i] == len(target):
            return i-len(target)+1
    return -1

# ex. leetcode 28.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)