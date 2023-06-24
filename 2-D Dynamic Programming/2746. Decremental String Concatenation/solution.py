class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        m = len(words)
        
        @lru_cache(None)
        def dfs(i, start, end):
            if i == m: return 0

            a, b = words[i][0], words[i][-1]
            
            n = len(words[i])
            
            # join str + words[i]
            res = dfs(i+1, start, b) + (n-1 if end == a else n)
            # join words[i] + str
            res = min(res, dfs(i+1, a, end) + (n-1 if b == start else n))
            return res
            
        return dfs(1, words[0][0], words[0][-1]) + len(words[0])