# take or skip strategy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(state, i):
            if i == n:
                res.append(state.copy())
                return

            dfs(state, i+1)
            state.append(nums[i])
            dfs(state, i+1)
            state.pop()
        dfs([], 0)
        return res