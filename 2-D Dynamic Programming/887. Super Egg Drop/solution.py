class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[k][i]: the maximum floor we can cover with k eggs and i try
        dp = [[0] * (N+1) for _ in range(K+1)]

        # base case:
        # dp[0][i] = 0, maximum floor we can check with certainty with 0 egg and i try
        # dp[k][0] = 0, maximum floor we can check with certainty with k egg and i try

        for i in range(1, N+1): # keep incrementing i to find minimum i that can cover n floor
            for k in range(1, K+1):
                # check x floor with i-th try
                # if egg breaks, the maximum floor we can cover is same as dp[k-1][i-1]
                # dp[k][i] = dp[k-1][i-1]
                # if egg not breaks, keep trying with k eggs and i-1 try and we check 1 floor with certainty
                # dp[k][i] = dp[k][i-1] + 1
                dp[k][i] = dp[k-1][i-1] + (dp[k][i-1]+1)
            if dp[k][i] >= N: return i
        return N # redundant but the maximum try we need is N
