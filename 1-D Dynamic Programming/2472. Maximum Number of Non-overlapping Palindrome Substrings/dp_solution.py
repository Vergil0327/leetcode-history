# Top-down with Memorization + Greedy
class Solution:
    @functools.lru_cache(None)
    def isPal(self, s, l, r):
        if r >= len(s) or s[l] != s[r]: return False
        
        if l < r:
            return self.isPal(s, l+1, r-1)
        else:
            return True

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i+k > n: return 0
            
            cnt = dfs(i+1)
            # for j in range(i+k-1, n):
            #     if self.isPal(s, i, j):
            #         cnt = max(cnt, 1 + dfs(j+1))

            # we only need to find minimum valid length palindrome (odd & even length),
            # since what we want is "maximum" number of palindromes
            if self.isPal(s, i, i+k-1):
                cnt = max(cnt, 1 + dfs(i+k))
            if self.isPal(s, i, i+k):
                cnt = max(cnt, 1+dfs(i+k+1))
            return cnt
        return dfs(0)

# Top-down with Memorization
class SolutionTLE:
    @functools.lru_cache(None)
    def isPal(self, s, l, r):
        if r >= len(s) or s[l] != s[r]: return False
        
        if l < r:
            return self.isPal(s, l+1, r-1)
        else:
            return True

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i+k > n: return 0
            
            cnt = dfs(i+1)
            for j in range(i+k-1, n):
                if self.isPal(s, i, j):
                    cnt = max(cnt, 1 + dfs(j+1))

            return cnt
        return dfs(0)