class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        if n == 3:
            return max(nums) + min(nums)

        @cache
        def dfs(i, candidates):
            candidates = list(candidates)
            while i < n and len(candidates) < 3:
                candidates.append(i)
                i += 1

            if len(candidates) <= 2:
                return max(nums[idx] for idx in candidates)
            else:
                # remove candidates[0], candidates[1]
                cost = max(nums[candidates[0]], nums[candidates[1]])
                x = dfs(i, (candidates[2],)) + cost
                # remove candidates[0], candidates[2]
                cost = max(nums[candidates[0]], nums[candidates[2]])
                y = dfs(i, (candidates[1],)) + cost
                # remove candidates[1], candidates[2]
                cost = max(nums[candidates[1]], nums[candidates[2]])
                z = dfs(i, (candidates[0],)) + cost

                return min(x, y, z)
        return dfs(0, ())
