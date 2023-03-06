from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp[i][0]: the maximum sum without square considering arr[:i]
        # dp[i][1]: the maximum sum with square arr[i] considering arr[:i]

        n = len(arr)
        dp = [[0, 0] for _ in range(n+1)] # 1-indexed

        arr = [0] + arr # shift to 1-indexed to match dp[i]
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i-1][0] + arr[i]**2, arr[i]**2, dp[i-1][1] + arr[i])
        
        return max(dp[i][1] for i in range(1, n+1))


