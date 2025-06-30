class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)

        def findLCP(s, t):
            lcp = 0
            for i in range(min(len(s), len(t))):
                if s[i] == t[i]:
                    lcp += 1
                else:
                    break
            return lcp
        
        adjacentLcp = [] # List to store LCP between adjacent words
        for i in range(1, n):
            adjacentLcp.append(findLCP(words[i-1], words[i]))
        
        prefixLCP = [0] # longest common prefix of adjacent words
        for i in range(len(adjacentLcp)):
            prefixLCP.append(max(prefixLCP[-1], adjacentLcp[i]))

        suffixLCP = [0] * (len(adjacentLcp)+1) # longest common prefix of adjacent words
        for i in range(len(adjacentLcp)-1, -1, -1):
            suffixLCP[i] = max(suffixLCP[i+1], adjacentLcp[i])

        res = [0] * n
        if n == 1: return res

        res[0] = suffixLCP[1]
        res[n-1] = prefixLCP[-2]

        for i in range(1, n-1):
            res[i] = max(findLCP(words[i-1], words[i+1]), prefixLCP[i-1], suffixLCP[i+1])
        return res