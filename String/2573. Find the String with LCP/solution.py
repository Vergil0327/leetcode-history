class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # lcp[i][j]: length of common prefix word[i:] and word[j]
        n = len(lcp)
        words = [""]*n
        shift = 0
        for i in range(n):
            if words[i]: continue
            for j in range(n):
                if words[j]: continue
                # words[i:i+lcp[i][j]] == words[j:j+lcp[i][j]]
                # -> words[i] == words[j]
                if lcp[i][j] > 0:
                    words[i] = chr(ord('a')+shift) if shift < 26 else ""
                    words[j] = words[i]
            shift += 1

        for i in range(n):
            for j in range(n):
                # example 3
                if i+lcp[i][j] > n or j+lcp[i][j] > n: return ""
                
                if words[i] == words[j]:
                    # case: [[2,1],[0,1]]
                    if lcp[i][j] == 0: return ""
                    # case: [[4,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
                    if i<n-1 and j<n-1 and lcp[i][j] != lcp[i+1][j+1]+1:
                        return ""
                else:
                    if lcp[i][j] != 0: return ""
                    if i<n-1 and j<n-1 and lcp[i][j] == lcp[i+1][j+1]+1:
                        return ""
        
        # final case
        ans = "".join(words)
        if len(ans) != n: return ""
        return ans