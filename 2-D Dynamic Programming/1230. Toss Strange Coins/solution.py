from typing import List

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)

        prob = [0] + prob # to 1-indexed

        # dp[i][j]: the probability that `j` coins facing heads considering tossing first `i` coins
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1 # first 0 coins to make 0 coins face head -> prob = 1

        for i in range(1, n+1):
            p = prob[i]
            for j in range(min(i, target)+1):
                # facing head: p
                # not facing head: 1-p
                # dp[i][j] state can comse from these two states: facing head & not facing head
                dp[i][j] = dp[i-1][j] * (1-p) + (dp[i-1][j-1] if j-1 >= 0 else 0) * p
        return dp[n][target]