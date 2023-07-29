class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000: return 1
        @lru_cache(None)
        def dfs(a, b):
            if a > 0 and b <= 0: return 0
            if a <= 0 and b > 0: return 1
            if a <= 0 and b <= 0: return 0.5

            prob = 0
            prob += dfs(a-100, b) * 0.25
            prob += dfs(a-75, b-25) * 0.25
            prob += dfs(a-50, b-50) * 0.25
            prob += dfs(a-25, b-75) * 0.25
            return prob
        return dfs(n, n)