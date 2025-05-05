class Solution:
    def minTravelTime(self, L: int, n: int, K: int, position: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, k, merge_start):
            if i == n-1:
                return 0 if k == 0 else inf

            rate = sum(time[tt] for tt in range(merge_start, i+1))
            res = inf
            for next_pos in range(i+1, min(n-1, i+1+k)+1):
                merges = next_pos - i - 1
                distance = position[next_pos] - position[i]

                res = min(res, dfs(next_pos, k - merges, i+1) + distance * rate) # merge {i+1, i+2, ..., next_pos-1} with next_pos
            return res

        ans = dfs(0, K, 0)
        dfs.cache_clear()
        return ans