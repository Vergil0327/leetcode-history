# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/discuss/2809337/PythonC%2B%2B-recursive-and-iterative-DP-solutions-(explained)
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
        
        # dp[i]: the maximum number of substrings s[i:]
        dp = [0]* (n+1)
        for i in range(k, n+1):
            dp[i] = dp[i-1]
            if self.isPal(s, i-k, i-1):
                dp[i] = max(dp[i], 1+ dp[i-k])
            # i-k-1 >= 0 avoid out-of-bound
            if i-k-1 >=0 and self.isPal(s, i-k-1, i-1):
                dp[i] = max(dp[i], 1+ dp[i-k-1])

        return dp[n]