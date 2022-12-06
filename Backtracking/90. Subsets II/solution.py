class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(state, i):
            if i == len(nums):
                res.append(state.copy())
                return

            # take current and don't take it anymore to prevent duplicate
            state.append(nums[i])
            dfs(state, i+1)
            state.pop()

            # skip current one
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            dfs(state, i+1)

        dfs([], 0)
        return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def dfs(state, i):
            res.append(state.copy())

            for j in range(i, n):
                # skip duplicate num
                if j > i and nums[j] == nums[j-1]: continue
                state.append(nums[j])
                dfs(state, j+1)
                state.pop()
        dfs([], 0)
        return res
