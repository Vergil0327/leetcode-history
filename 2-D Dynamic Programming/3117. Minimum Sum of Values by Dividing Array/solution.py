class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        @cache
        def dfs(i, j, AND):
            if j == m:
                if i == n: return 0
                return inf
            if i == n: return inf
            cur = nums[i] & AND if AND != -1 else nums[i]

            res = dfs(i+1, j, cur)
            if cur == andValues[j]:
                res = min(res, dfs(i+1, j+1, -1) + nums[i])
            return res

        ans = dfs(0, 0, -1)
        return ans if ans < inf else -1
