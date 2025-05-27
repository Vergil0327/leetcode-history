class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        char = [ord(c) - ord("a") for c in s]

        @cache
        def empty(l, r):
            # Can S[l..r] be removed completely?
            if l > r:
                return True
            if abs(char[l] - char[r]) in [1, ord("z")-ord("a")] and empty(l + 1, r - 1):
                return True
            return any(empty(l, k) and empty(k + 1, r) for k in range(l + 1, r, 2))

        @cache
        def dfs(i):
            # Answer for S[i:]
            if i >= n: return ""

            ans = s[i] + dfs(i + 1)
            for j in range(i + 1, n, 2):
                if empty(i, j):
                    ans = min(ans, dfs(j + 1))
            return ans

        return dfs(0)