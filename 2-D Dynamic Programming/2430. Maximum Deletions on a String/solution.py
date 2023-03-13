class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        cache = {}
        def dfs(i):
            if i >= n: return 0
            if i in cache: return cache[i]

            cache[i] = 1
            numCharacters = (n-i)//2 + 1
            for j in range(1, numCharacters):
                if s[i:i+j] == s[i+j:i+2*j]:
                    cache[i] = max(cache[i], dfs(i+j)+1)
            
            return cache[i]
        return dfs(0)

        # TLE
        # def dfs(s):
        #     if not s: return 0
        #     if s in cache: return cache[s]
        #     n = len(s)

        #     res = dfs("")+1
        #     for i in range(1, n+1):
        #         if s[:i] == s[i:2*i]:
        #             res = max(res, dfs(s[i:]) + 1)
        #     cache[s] = res
        #     return res
        # return dfs(s)

class Solution_BottomUp:
    def deleteString(self, s: str) -> int:
        n = len(s)

        # the legnth of longest common subarray for s[:i]
        lcs = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                # [XXX][XXX]XXXXXX
                #  i    j
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i+1][j+1] + 1

        # dp[i]: the maximum number of operations needed to delete all of s[i:n-1]
        dp = [1] * 4004
        n = len(s)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # if s[i:j] == s[j:j+j-i]: -> 預先處理, 又是另一個DP問題，雙序列DP
                if lcs[i][j] >= j-i:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[0]
    
    """
    其實上面兩個DP能結合在一起
    """
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1: return n

        # dp[i]: the maximum number of operations needed to delete all of s[i:n-1]
        dp = [1] * 4004
        # the legnth of longest common subarray for s[:i]
        lcs = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i+1][j+1] + 1
                if lcs[i][j] >= j-i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]

    