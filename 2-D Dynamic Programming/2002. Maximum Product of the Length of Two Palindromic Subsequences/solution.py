class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def findPalindrome(s):
            if not s: return 0

            m = len(s)
            dp = [[0]*m for _ in range(m)]
            for i in range(m):
                dp[i][i] = 1
            for i in range(m-1):
                if s[i] == s[i+1]:
                    dp[i][i+1] = 2
                else:
                    dp[i][i+1] = 1
            for length in range(3, m+1):
                for i in range(m-length+1):
                    j = i+length-1
                    if s[i] == s[j]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            return dp[0][m-1]

        self.res = 0
        def dfs(i, sub1, sub2):
            if i == n:
                if not sub1 or not sub2: return

                p = findPalindrome(sub1) * findPalindrome(sub2)
                self.res = max(self.res, p)
                return

            # pick for subseq.1
            dfs(i+1, sub1+s[i], sub2)

            # skip for subseq.1
            dfs(i+1, sub1, sub2+s[i])
        dfs(0, "", "")
        return self.res