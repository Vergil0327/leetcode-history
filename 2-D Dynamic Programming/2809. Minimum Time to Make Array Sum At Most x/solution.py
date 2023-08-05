class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)

        arr = sorted(zip(nums2, nums1))

        dp = [[0]*(n+1) for _ in range(n+1)]
        for i, (num2, num1) in enumerate(arr, start=1):
            for j in range(1, i+1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + num2*j + num1)

        sum1 = sum(nums1)
        sum2 = sum(nums2)
        for t in range(n+1):
            if sum1 + sum2*t - dp[n][t] <= x: return t
        return -1