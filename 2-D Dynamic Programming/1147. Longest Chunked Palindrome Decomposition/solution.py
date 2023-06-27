class Solution:
    def longestDecomposition(self, text: str) -> int:
        @lru_cache(None)
        def dfs(text):
            n = len(text)
            res = 1 if text else 0
            for i in range(1, n//2+1):
                j = n-i
                if i > j: break
                if text[:i] == text[j:]:
                    res = max(res, dfs(text[i:j]) + 2)
            return res
        
        return dfs(text)