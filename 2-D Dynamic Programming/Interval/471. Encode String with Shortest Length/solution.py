class Solution:
    def encode(self, s: str) -> str:
        n = len(s)

        dp = [[""] * n for _ in range(n)]

        def encode(l, r):
            substr = s[l:r+1]
            m = len(substr)
            res = substr
            for length in range(1, m):
                if m%length != 0: continue

                canRepeated = True
                for k in range(0, m-length+1, length):
                   if substr[k:k+length] != substr[:length]:
                      canRepeated = False
                      break
                if not canRepeated: continue

                # critical, easily wrong by writing like
                # encoded = f"{m//length}[{s[l:l+length]}]"
                encoded = f"{m//length}[{dp[l][l+length-1]}]"

                if len(encoded) < len(res):
                   res = encoded
            return res
                    
        
        for length in range(1, n+1):
            for i in range(n-length+1): # j = i+length-1<n
                if length == 1:
                   dp[i][i]  = s[i]
                   continue
                
                j = i+length-1
                dp[i][j] = encode(i, j)

                for k in range(i, j):
                   if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                      dp[i][j] = dp[i][k] + dp[k+1][j]

        return dp[0][n-1]
