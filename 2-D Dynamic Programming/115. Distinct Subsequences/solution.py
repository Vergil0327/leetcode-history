class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # use dfs to explore all the possibility
        # i is index at s and j is index at t, keep comparing s[i:] and t[j:]
        @functools.lru_cache(None)
        def dfs(i, j):
            if j == n: return 1 # found matched
            if i == m: return 0
            
            num = dfs(i+1, j) # skip current character and compare rest of s and t
            if s[i] == t[j]: # take current character if valid and keep comparing rest of s and t
                num += dfs(i+1, j+1)
            return num
        
        return dfs(0, 0)