class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def dfs(state, i):
            if sum(state) == target:
                res.append(state.copy())
                return
            if i == n or sum(state) > target:
                return

            state.append(nums[i])
            dfs(state, i+1)
            state.pop()

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(state, i+1)
        dfs([], 0)
        return res