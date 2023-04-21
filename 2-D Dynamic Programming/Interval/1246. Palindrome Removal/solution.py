from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)

        dp = [[float("inf")]*n for _ in range(n)]

        # length=1
        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                dp[i][j] = dp[i][j-1] + 1
                
                for k in range(i, j):
                    if arr[k] == arr[j]:
                        dp[i][j] = min(dp[i][j], (dp[i][k-1] if k-1 >= i else 0) + (dp[k+1][j-1] if k+1 <= j-1 else 1))
                        # or dp[i][j] = dp[i][k-1] + max(dp[k+1][j-1], 1)

        return dp[0][n-1]

        # X [X X X X X X X] 
        # i  k           j
        # X X X X [X][X] 
        # i        k  j
        # X X X X [X] {X X X X} [X] 
        # i        k             j
