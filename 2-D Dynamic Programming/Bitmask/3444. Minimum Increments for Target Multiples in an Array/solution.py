class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        target = list(set(target)) # remove duplicate
        target.sort(reverse=True)
        nums.sort(reverse=True)

        n, m = len(nums), len(target)
        inf = float('inf')

        @lru_cache(None)
        def dfs(i, state):
            if state.bit_count() == m: return 0
            if i >= n: return 0 if state.bit_count() == m else inf

            res = dfs(i+1, state)

            for j in range(m):
                if (state>>j)&1: continue
                
                x = ceil(nums[i]/target[j])
                multiple = target[j]*x

                inc = multiple - nums[i]
                newState = state | (1<<j)
                for k in range(j+1, m):
                    if multiple % target[k] == 0:
                        newState |= (1<<k)
                res = min(res, dfs(i+1, newState) + inc)
            return res

        return dfs(0, 0)