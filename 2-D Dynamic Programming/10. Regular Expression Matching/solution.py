# Top-Down with Memorization
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # i, j means we discuss matching s[i:] with p[j:]
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == n:
                return True
            # s[i:] = "XXXX", impossible to match empty string ""
            if j == n: return False
            if i == m:
                # s = "", and p = "?*"
                if j+1<n and p[j+1] == "*":
                    return dfs(i, j+2)
                return False
            
            if j+1<n and p[j+1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    return dfs(i+1, j) or dfs(i, j+2) # use * to match s[i] or not use * to match s[i]
                else:
                    return dfs(i, j+2)
            else:
                if s[i] == p[j] or p[j] == ".":
                    return dfs(i+1, j+1)
                else:
                    return False
                
        return dfs(0, 0)

# Bottom-Up DP
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] : matching result where p[:j] cover the entire s[:i]
        dp = [[False] * (n+1) for _ in range(m+1)]
        # easier to handle index in for-range iteration if we append placeholder to shift index.
        s = "#" + s
        p = "#" + p
        
        # Base Case
        dp[0][0] = True
        # dp[i][0] = False, where i from 0 to m. s[:i] = "XXXX" and p[:j] = ""
        for j in range(1, n+1, 2):
            if j+1<n+1 and p[j+1] == "*":
                dp[0][j] = True
                dp[0][j+1] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j] == "*":
                    # choose NOT to use * to match s[i]
                    if j-2 >=0:
                        dp[i][j] = dp[i][j-2]
                    
                    # use * with preceding character to match s[i]
                    if s[i] == p[j-1] or p[j-1] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                    
                    # also update p[:j-1]'s DP
                    dp[i][j-1] = dp[i][j]
                else: # just string matching
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        
        return dp[m][n]