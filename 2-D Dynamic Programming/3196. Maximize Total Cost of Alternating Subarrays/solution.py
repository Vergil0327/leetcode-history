class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, sign):
            if i == n: return 0

            # split
            res = dfs(i+1, 1)
            res = max(res, dfs(i+1, -1 * sign))
            return res + nums[i]*sign
        return dfs(0, 1)
