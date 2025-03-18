class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        if all(nums[i] == 0 for i in range(n)): return 0

        # dp[i][num]: whether the i-th element which equals num can be reduce to zero
        dp = [[False]*(1000+1) for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][0] = True

        for k in range(m):
            l, r, val = queries[k]
            for i in range(l, r+1):
                for num in range(1000, -1, -1):
                    if num-val >= 0 and dp[i][num-val]:
                        dp[i][num] = True
            if all(dp[j][nums[j]] for j in range(n)): return k+1
        return -1
