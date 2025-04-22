@cache
def isSubsequence(s1, s2):
    i = j = 0

    while i < len(s1) and j < len(s2):
        if s2[j] == s1[i]:
            i += 1
        j += 1

    return i == len(s1)

# brute force
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:                
        length = 0
        for i in range(len(strs)):
            n = len(strs[i])
            state = (1<<n)-1
            submask = state
            
            while submask > 0:
                subseq = "".join([strs[i][j] for j in range(n) if (submask>>j)&1])
                if len(subseq) > length:
                    valid = True
                    for k in range(len(strs)):
                        if k == i: continue
                        if isSubsequence(subseq, strs[k]):
                            valid = False
                            break
                    if valid:
                        length = max(length, len(subseq))
                
                submask = (submask-1)&state
            
        return length if length > 0 else -1
                
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        freqs = Counter(strs)
        result = -1

        for s in strs:
            # we only have one copy of s and it is greater than the max already found -> candidate
            # subsequence
            if freqs[s] == 1 and len(s) > result:
                unique = not any([isSubseq(s, x) for x in strs if x != s])
                if unique:
                    result = len(s)

        return result