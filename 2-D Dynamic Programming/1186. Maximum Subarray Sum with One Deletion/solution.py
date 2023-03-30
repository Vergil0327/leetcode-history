class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        # dp[i][0]: maximum sum for a non-empty subarray without 1 deletion
        # dp[i][1]: maximum sum for a non-empty subarray with 1 deletion
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = 0

        res = arr[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
            res = max(res, max(dp[i][0], dp[i][1]))
        return res