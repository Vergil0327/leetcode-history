class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        dp = [1] * n # dp[i]: the longest length of LIS ended at i-th element

        m = len(strs)
        def canAppendLIS(x, y):
            for i in range(m):
                if strs[i][x] > strs[i][y]: return False
            return True
        
        for i in range(n):
            for j in range(i):
                if canAppendLIS(j, i):
                    dp[i] = max(dp[i], dp[j] + 1)

        maxLen = max(dp)
        return n-maxLen