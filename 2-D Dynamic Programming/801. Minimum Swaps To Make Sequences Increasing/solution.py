class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # dp[i][didSwap, 0 or 1]: the minimum number of swaps to make nums1[:i] and nums2[:i] strictly increasing which didSwap = 0 means we don't swap nums1[i] with nums2[i], whereas didSwap = 1 means we swap nums1[i] with nums2[i]
        dp = [[inf]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1

        for i in range(1, n):
            # don't swap nums1[i] with nums2[i] at i-th round
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]: # if we don't swap at last round
                dp[i][0] = min(dp[i][0], dp[i-1][0])
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]: # if we swap at last round
                dp[i][0] = min(dp[i][0], dp[i-1][1])

            # need to swap nums1[i] with nums2[i] at i-th round
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]: # if we don't swap at last round
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]: # if we swap at last round
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
        return min(dp[-1])