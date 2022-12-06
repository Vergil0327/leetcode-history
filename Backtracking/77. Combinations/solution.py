# after choosing current number, we only can choose number after current
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(state, i):
            if len(state) == k:
                res.append(state.copy())
                return

            for j in range(i, n+1):
                state.append(j)
                dfs(state, j+1)
                state.pop()
        dfs([], 1)
        return res