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


class SolutionBottomUpOptimized:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] : The matching for s[:i] compared with j[:j]
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # because "" == ""
        
        # dp[0][x]: s = "" and p[:x] = "XXX", only True for p[:x] = "*******" where * shows x times
        for x in range(1, n+1):
            if p[x-1] == "*":
                dp[0][x] = True
            else:
                break
            
        # dp[x][0]: p = "" -> must be False
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # s[:i] = "XXXXXXXXX" X
                    #             i-1     i
                    # p[:j] = "YYYYYYYY" Y
                    # if s[0-i][j-1] is True, which means s[:k] matched with p[:j-1] where k from 0 to i
                    # then, dp[i][j] must be true because dp[k][j-1] is true and current p[j] == "*" which is always match any character
                    # for k in range(0, i+1):
                    #     if dp[k][j-1]: dp[i][j] = True
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]
class SolutionBottomUpTLE:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] : The matching for s[:i] compared with j[:j]
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True # because "" == ""
        
        # dp[0][x]: s = "" and p[:x] = "XXX", only True for p[:x] = "*******" where * shows x times
        for x in range(1, n+1):
            if p[x-1] == "*":
                dp[0][x] = True
            else:
                break
            
        # dp[x][0]: p = "" -> must be False
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    # s[:i] = "XXXXXXXXX" X
                    #             i-1     i
                    # p[:j] = "YYYYYYYY" Y
                    # if s[0-i][j-1] is True, which means s[:k] matched with p[:j-1] where k from 0 to i
                    # then, dp[i][j] must be true because dp[k][j-1] is true and current p[j] == "*" which is always match any character
                    for k in range(0, i+1):
                        if dp[k][j-1]: dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[m][n]