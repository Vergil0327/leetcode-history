# Memory Limit Exceeded !!!
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp[i][j]: the length of shortest common supersequence considering str1[0:i] and str2[0:j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = 0
        dpstrings = [[""]*(n+1) for _ in range(m+1)]
        
        # shift str1 and str2 to 1-indexed to match dp state
        str1 = "#" + str1
        str2 = "#" + str2

        for i in range(1, m+1):
            dp[i][0] = i
            dpstrings[i][0] = str1[1:i+1]
        for j in range(1, n+1):
            dp[0][j] = j
            dpstrings[0][j] = str2[1:j+1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    dpstrings[i][j] = dpstrings[i-1][j-1] + str1[i]
                else:
                    # dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                    if dp[i-1][j]+1 < dp[i][j-1]+1:
                        dp[i][j] = dp[i-1][j] + 1
                        dpstrings[i][j] = dpstrings[i-1][j] + str1[i]
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                        dpstrings[i][j] = dpstrings[i][j-1] + str2[j]
        return dpstrings[m][n]

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp[i][j]: the length of shortest common supersequence considering str1[0:i] and str2[0:j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # base case
        dp[0][0] = 0
        
        # shift str1 and str2 to 1-indexed to match dp state
        str1 = "#" + str1
        str2 = "#" + str2

        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    # dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                    if dp[i-1][j]+1 < dp[i][j-1]+1:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1

        res = [""] * dp[m][n]
        i, j, k = m, n, dp[m][n]-1
        while i > 0 and j > 0:
            if str1[i] == str2[j]:
                res[k] = str1[i]
                i, j, k = i-1, j-1, k-1
            elif dp[i][j] == dp[i-1][j]+1:
                res[k] = str1[i]
                i, k = i-1, k-1
            else: # dp[i][j] == dp[i][j-1]+1:
                res[k] = str2[j]
                j, k = j-1, k-1

        while i > 0:
            res[k] = str1[i]
            i, k = i-1, k-1
        while j > 0:
            res[k] = str2[j]
            j, k = j-1, k-1

        return "".join(res)