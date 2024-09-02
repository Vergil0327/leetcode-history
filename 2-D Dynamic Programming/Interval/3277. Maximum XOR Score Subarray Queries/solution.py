class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        score = [[0]*n for _ in range(n)]
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            score[i][i] = dp[i][i] = nums[i]

        for length in range(2, n+1):
            for i in range(n-length+1): # j = i+length-1 < n
                j = i+length-1
                score[i][j] = score[i][j-1] ^ score[i+1][j]

                dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1], score[i][j])
                

        return [dp[l][r] for l, r in queries]