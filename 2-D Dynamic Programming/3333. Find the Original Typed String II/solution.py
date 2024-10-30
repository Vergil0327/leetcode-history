from itertools import accumulate

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(word)

        consecutive = []
        cnt = 1
        for i in range(n-1):
            if word[i] == word[i+1]:
                cnt += 1
            else:
                consecutive.append(cnt)
                cnt = 1
        consecutive.append(cnt)
        
        m = len(consecutive)

        total_ways = 1
        for size in consecutive:
            total_ways = (total_ways * size) % mod

        if k <= m: return total_ways
        
        dp = [[0]* k for _ in range(m+1)] # 1-indexed
        dp[0][0] = 1
        for i in range(1, m+1):
            prefix_sum_prev_dp = list(accumulate(dp[i-1], lambda x, y: (x+y)%mod, initial=0))

            for j in range(k):
                # for seg in range(1, min(j, consecutive[i-1])+1):
                #     dp[i][j] += dp[i-1][j - seg]
                #     dp[i][j] %= mod
                dp[i][j] =  prefix_sum_prev_dp[j] - prefix_sum_prev_dp[j - min(j, consecutive[i-1])]
                dp[i][j] %= mod

        return ((total_ways - sum(dp[m])) + mod) % mod