
"""
X X X X X X X [X] => SUM = max([X]) * (i-j+1)
                   i
X X X X X X [X X] => SUM = max([X X]) * (i-j+1)
             j i
X X X X X [X X X] => SUM = max([X X]) * (i-j+1)
           j   i
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        dp = [0] * n
        for i in range(n):
            MAX = -inf
            for j in range(i, max(-1, i-k), -1):
                MAX = max(MAX, arr[j])
                dp[i] = max(dp[i], (dp[j-1] if j-1 >=0 else 0) + MAX * (i-j+1))
        return dp[n-1]
