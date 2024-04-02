class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i, state, change):
            if i == n: return 1 if state > 0 else 0
            
            bit = ord(s[i])-ord("a")
            new_state = state|(1<<bit)

            res = 0
            if new_state.bit_count() > k:
                res = max(res, dfs(i+1, 1<<bit, change)+1)
            else:
                res = dfs(i+1, new_state, change)

            if not change:
                for j in range(26):
                    if j == bit: continue
                    new_state = state|(1<<j)
                    if new_state.bit_count() > k:
                        res = max(res, dfs(i+1, (1<<j), True)+1)
                    else:
                        res = max(res, dfs(i+1, new_state, True))

            return res
        return dfs(0, 0, False)
