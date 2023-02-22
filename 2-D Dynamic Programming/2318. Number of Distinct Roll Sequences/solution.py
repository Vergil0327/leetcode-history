class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6 # 1, 2, 3, 4, 5, 6

        MOD = int(1e9+7)
        dp = [[[0]*7 for _ in range(7)] for _ in range(n+1)]

        count = 0
        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and gcd(i,j) == 1:
                    dp[2][i][j] = 1
                    count += 1
        if n == 2: return count

        # Rolls: X X X X X X X last2 last cur
        for i in range(3, n+1):
            for cur in range(1, 7):
                for last in range(1, 7):
                    if cur == last: continue
                    if gcd(cur, last) != 1: continue
                    for last2 in range(1, 7):
                        if cur != last2:
                            dp[i][cur][last] += dp[i-1][last][last2]
                            dp[i][cur][last] %= MOD
        total = 0
        for i in range(1, 7):
            for j in range(1, 7):
                total += dp[n][i][j]
                total %= MOD
        return total
    
# Optimized
class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6 # 1, 2, 3, 4, 5, 6

        GCD_One = [[] for _ in range(7)]
        for i in range(1, 7):
            for j in range(1, 7):
                if gcd(i, j) == 1:
                    GCD_One[i].append(j)

        MOD = int(1e9+7)
        dp = [[[0]*7 for _ in range(7)] for _ in range(n+1)]

        count = 0
        for i in range(1, 7):
            for j in GCD_One[i]:
                if i != j:
                    dp[2][i][j] = 1
                    count += 1
        if n == 2: return count

        # Rolls: X X X X X X X last2 last cur
        for i in range(3, n+1):
            for cur in range(1, 7):
                for last in GCD_One[cur]:
                    if cur == last: continue
                    for last2 in range(1, 7):
                        if cur != last2:
                            dp[i][cur][last] += dp[i-1][last][last2]
                            dp[i][cur][last] %= MOD
        
        total = 0
        for i in range(1, 7):
            for j in range(1, 7):
                total += dp[n][i][j]
                total %= MOD
        return total
    

class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = int(1e9+7)

        @lru_cache(None)
        def dfs(n, last, last2):
            if n == 0: return 1

            res = 0
            for cur in range(1, 7):
                if cur != last and cur!= last2 and gcd(cur, last) == 1:    
                    res += dfs(n-1, cur, last)
            return res % MOD
        return dfs(n, -1, -1)