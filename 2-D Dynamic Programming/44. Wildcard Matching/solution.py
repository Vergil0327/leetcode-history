class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == n: return True
            if j == n: return False
            if i == m:
                if p[j] == "*":
                    return dfs(i, j+1)
                else:
                    return False
            
            if s[i] == p[j] or p[j] == "?":
                return dfs(i+1, j+1)
            elif p[j] == "*": # we can use * to match or we don't use *
                return dfs(i+1, j) or dfs(i, j+1)
            else:
                return False
        return dfs(0, 0)