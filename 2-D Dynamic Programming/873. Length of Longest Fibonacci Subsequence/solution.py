class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        val2idx = {v:i for i, v in enumerate(arr)}

        @lru_cache(None)
        def dfs(i, prev=-1):
            length = 1
            if prev == -1:
                for j in range(i+1, n):
                    if arr[i]+arr[j] in val2idx:
                        length = max(length, dfs(val2idx[arr[i]+arr[j]], arr[j])+2)
            elif prev+arr[i] in val2idx:
                idx = val2idx[prev+arr[i]]
                length = max(length, dfs(idx, arr[i])+1)
            return length

        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res if res > 2 else 0
