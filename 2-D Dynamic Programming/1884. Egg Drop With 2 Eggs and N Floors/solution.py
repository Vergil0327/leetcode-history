class Solution:
    @cache
    def twoEggDrop(self, n: int) -> int:
        if n == 1: return 1

        moves = inf
        for i in range(1, n+1):
            moves = min(moves, 1 + max(i-1, self.twoEggDrop(n-i)))
        return moves


class Solution:
    def twoEggDrop(self, n: int) -> int:
        # dp[k][i]: the maximum floor we can cover with k eggs and i try
        k = 2 # two eggs
        dp = [[0] * (n+1) for _ in range(k+1)]

        # base case:
        # dp[0][i] = 0, maximum floor we can check with certainty with 0 egg and i try
        # dp[k][0] = 0, maximum floor we can check with certainty with k egg and i try

        ops = 0
        while dp[k][ops] < n:
            ops += 1
            for kk in range(1, k+1):
                # if egg breaks, the maximum floor we can cover is same as dp[k-1][i-1]
                # - dp[k][i] = dp[k-1][i-1]
                # if egg not breaks, keep trying with k eggs and i-1 try and we check 1 floor with certainty
                # - dp[k][i] = dp[k][i-1] + 1
                dp[kk][ops] = dp[kk-1][ops-1] + (dp[kk][ops-1]+1)
        return ops
