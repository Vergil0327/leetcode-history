class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    prefix_dp[i] = max(prefix_dp[i], prefix_dp[j]+1)

        suffix_dp = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    suffix_dp[i] = max(suffix_dp[i], suffix_dp[j]+1)
        res = inf
        for i in range(1, n-1):
            pre = (i+1)-prefix_dp[i]
            suf = n-i-suffix_dp[i]
            if prefix_dp[i] > 1 and suffix_dp[i] > 1:
                res = min(res, pre+suf)
        return res
