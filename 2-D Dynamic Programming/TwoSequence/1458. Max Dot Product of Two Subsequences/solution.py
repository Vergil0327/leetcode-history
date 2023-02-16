class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[-inf] * (n+1) for _ in range(m+1)]
        dp[0][0] = 0

        # shift to 1-indexed to match dp[i][j]
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i][j], dp[i-1][j], nums1[i]*nums2[j])
                dp[i][j] = max(dp[i][j], dp[i][j-1], nums1[i]*nums2[j])
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+nums1[i]*nums2[j])

        return dp[m][n]