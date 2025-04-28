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

# return all the valid index of target in s
def kmpAll(s: str, target: str):
    n = len(s)

    # preprocess
    # longest prefix suffix
    lps = preprocess(target)

    # find target word in s
    res = []
    j = 0
    for i in range(n):
        while j > 0 and s[i] != target[j]:
            j = lps[j-1]
        j = j+int(s[i] == target[j])
        if j == len(target):
            j = lps[j-1]
            res.append(i-len(target)+1)
    return res

# ex. leetcode 28.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)
    

# version 2

def compute_lps(pattern):
    lps = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

# find all occurrences of pattern in text
def kmp(text, pattern):
    if not pattern: # pattern = "*"
        return list(range(len(text)+1))

    lps = compute_lps(pattern)
    res = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                res.append(i - j)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return res
