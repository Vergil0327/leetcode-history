"""
Key Logic Points

Initialization: Use -float('inf') for all states except when p=0.
This ensures you only build upon valid previous states and can handle negative results correctly.

Transitions:
dp[p][i-1][j]: Maximum score without using the current element from nums1.
dp[p][i][j-1]: Maximum score without using the current element from nums2.
dp[p-1][i-1][j-1] + prod: Maximum score by pairing the current two elements.

Complexity

Time: $O(k \cdot n \cdot m)$, which is $100^3 = 1,000,000$ operations—well within the limit.
Space: $O(k \cdot n \cdot m)$, but can be optimized to $O(k \cdot m)$ if necessary.
"""

class Solution:
    """
    This is a variation of the Matrix Chain Multiplication or LCS style DP.
    We define $dp[i][j][p]$ as the maximum score using exactly $p$ pairs from the first $i$ elements of nums1 and the first $j$ elements of nums2.
    """
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        
        # Initialize with -infinity because scores can be negative
        # dp[p][i][j] = max score using p pairs from nums1[:i] and nums2[:j]
        # We can optimize space to dp[p][j] since we only need the previous i
        INF = float('inf')
        dp = [[-INF] * (m + 1) for _ in range(k + 1)]
        
        # Base case: 0 pairs always gives 0 score
        for j in range(m + 1):
            dp[0][j] = 0
                    
        # Refined O(k * n * m) approach:
        # dp[p][i][j] is max score using p pairs from nums1[:i] and nums2[:j]
        dp = [[[-INF] * (m + 1) for _ in range(n + 1)] for _ in range(k + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                dp[0][i][j] = 0
        
        for p in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    # Option A: Skip nums1[i-1]
                    res = dp[p][i-1][j]
                    # Option B: Skip nums2[j-1]
                    res = max(res, dp[p][i][j-1])
                    # Option C: Match nums1[i-1] and nums2[j-1]
                    if dp[p-1][i-1][j-1] != -INF:
                        res = max(res, dp[p-1][i-1][j-1] + nums1[i-1] * nums2[j-1])
                    dp[p][i][j] = res
                    
        return dp[k][n][m]