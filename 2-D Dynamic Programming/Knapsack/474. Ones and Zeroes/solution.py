# 3-D DP
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [Counter(s) for s in strs]

        # dp[i][m][n]: the size of  the largest subset s.t. there are m 0's' and n 1's' at most.
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs))]

        zero, one = counters[0]["0"], counters[0]["1"]
        for mm in range(m+1):
            for nn in range(n+1):
                if mm-zero >= 0 and nn-one >= 0:
                    dp[0][mm][nn] = 1
                

        for i in range(1, len(strs)):
            zero, one = counters[i]["0"], counters[i]["1"]
            for mm in range(m+1):
                for nn in range(n+1):
                    dp[i][mm][nn] = max(dp[i][mm][nn], dp[i-1][mm][nn])

                    if mm-zero >= 0 and nn-one >= 0:
                        dp[i][mm][nn] = max(dp[i][mm][nn], dp[i-1][mm-zero][nn-one] + 1)
        
        return dp[len(strs)-1][m][n]

# 2-D DP
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [Counter(s) for s in strs]

        # dp[i][m][n]: the size of  the largest subset s.t. there are m 0's' and n 1's' at most.
        dp = [[0] * (n+1) for _ in range(m+1)]
        prevdp = [[0] * (n+1) for _ in range(m+1)]

        zero, one = counters[0]["0"], counters[0]["1"]
        for mm in range(m+1):
            for nn in range(n+1):
                if mm-zero >= 0 and nn-one >= 0:
                    prevdp[mm][nn] = 1
                
        for i in range(1, len(strs)):
            zero, one = counters[i]["0"], counters[i]["1"]
            for mm in range(m+1):
                for nn in range(n+1):
                    dp[mm][nn] = max(dp[mm][nn], prevdp[mm][nn])

                    if mm-zero >= 0 and nn-one >= 0:
                        dp[mm][nn] = max(dp[mm][nn], prevdp[mm-zero][nn-one] + 1)
            dp, prevdp = prevdp, dp
        return prevdp[m][n]
    
# Optimized
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [Counter(s) for s in strs]

        # dp[i][m][n]: the size of  the largest subset s.t. there are m 0's' and n 1's' at most.
        dp = [[0] * (n+1) for _ in range(m+1)]

        zero, one = counters[0]["0"], counters[0]["1"]
        for mm in range(m+1):
            for nn in range(n+1):
                if mm-zero >= 0 and nn-one >= 0:
                    dp[mm][nn] = 1

        for i in range(1, len(strs)):
            zero, one = counters[i]["0"], counters[i]["1"]
            for mm in range(m, zero-1, -1):
                for nn in range(n, one-1, -1):
                    dp[mm][nn] = max(dp[mm][nn], dp[mm-zero][nn-one] + 1)
        return dp[m][n]