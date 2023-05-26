class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        n, m = len(word1), len(word2)
        res = ""

        while i < n and j < m:
            if word1[i:] > word2[j:]:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
        
        if i < n:
            res += word1[i:]
        if j < m:
            res += word2[j:]
        return res