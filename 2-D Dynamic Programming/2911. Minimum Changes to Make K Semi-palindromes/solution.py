class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = [[1] for _ in range(n+1)]
        for d in range(2, n):
            for v in range(d+d, n+1, d):
                factors[v].append(d)
        
        changes = [[inf]*n for _ in range(n)]
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                # [{X X X} {X X X} {X X X}]
                #   i                   j
                for d in factors[length]:
                    cnt = 0
                    for offset in range(d):
                        l, r = i+offset, i+offset+length-d
                        while l < r:
                            if s[l] != s[r]:
                                cnt += 1
                            l, r = l+d, r-d
                    changes[i][j] = min(changes[i][j], cnt)
                    
        dp = [[inf]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1): # 1-indexed
            for kk in range(1, k+1):
                for j in range(i-1): # j 0-indexed, it's invalid for length=1, therefore, j <= i-2
                    dp[i][kk] = min(dp[i][kk], dp[j][kk-1]+changes[j][i-1])
            
        return dp[n][k]