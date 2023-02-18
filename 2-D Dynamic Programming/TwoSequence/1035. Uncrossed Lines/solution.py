class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        # dp[i][j]: the maximum number of uncrossed lines considering nums1[0:i] and nums2[0:j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # base case
        # dp[0][0] = dp[0][j] = dp[i][0] = 0

        # shift to 1-indexed
        nums1 = [0] + nums1
        nums2 = [0] + nums2

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]