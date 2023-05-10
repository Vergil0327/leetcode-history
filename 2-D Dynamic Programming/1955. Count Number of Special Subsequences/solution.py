class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        dp = [[0]*3 for _ in range(n+1)] # 1-indexed
        nums = [-inf] + nums # shift to 1-indexed

        for i in range(1, n+1):
            if nums[i] == 0:
                dp[i][0] += dp[i-1][0]*2+1 # 接在0後面 / 不接在0後面 / 自立門戶(new subseq.)
                dp[i][0] %= mod
                dp[i][1] = dp[i-1][1]
                dp[i][2] = dp[i-1][2]
            if nums[i] == 1:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][0] + dp[i-1][1]*2 # 可接在結尾為0的subseq. / 加或不加在結尾1的subseq.
                dp[i][1] %= mod
                dp[i][2] = dp[i-1][2]
            if nums[i] == 2:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
                dp[i][2] = dp[i-1][1] + dp[i-1][2]*2 # 可接在結尾為1的subseq. / 加或不加在結尾為2的subseq
                dp[i][2] %= mod

        return dp[n][2]
