class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        def calLen(length):
            if length == 0: return 0
            elif length == 1: return 1
            elif length < 10: return 2
            elif length < 100: return 3
            else:
                return 4

        @cache
        def dfs(i, k, prev, cnt):
            if i == n:
                return calLen(cnt)

            res = inf
            # delete s[i]
            if k > 0:
                res = dfs(i+1, k-1, prev, cnt)

            # keep s[i]
            if s[i] == prev:
                res = min(res, dfs(i+1, k, prev, cnt+1))
            else:
                res = min(res, dfs(i+1, k, s[i], 1) + calLen(cnt))
            return res
        return dfs(0, k, "#", 0)