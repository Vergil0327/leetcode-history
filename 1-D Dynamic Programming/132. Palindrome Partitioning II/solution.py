"""
Intuition:
we count number of valid palindromes instead.
`min cut = min(number of palindromes) - 1`

thanks to [this solution](https://leetcode.com/problems/palindrome-partitioning-ii/discuss/1388628/Python-Simple-Top-down-DP-Clean-and-Concise)
we got almost the same solution excluding implementation of `isPalindrome`
the difference is I used iteration method to implement `isPalindrome(l, r)` and I got TLE. :(

we can see that if we also use memorization technique to `isPalinedrome`, we can reduce lots of repetitive caluculation

Complexity

Time: O(N^2)
    Time complexity for isPalindrome(l, r) is O(N^2)
    Time complexity for dfs(i) is O(N^2)
    Since we cache all the N^2 results from isPalindrome, time complexity of isPalindrome in minCut becomes O(1)
    So total time complexity is O(N^2)
Space: O(N^2)
"""
class Solution:
    def minCut(self, s: str) -> int: 
        # TLE
        # def isPalindrome(l, r): # [l, r], both inclusive
        #     if s[l] != s[r]: return False
        #     while l < r:
        #         l+=1
        #         r-=1
        #         if s[l] != s[r]: return False
        #     return True

        @functools.lru_cache(None)
        def isPalindrome(l, r): # [l, r], both inclusive
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        n = len(s)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            # palindrome groups
            groups = float('inf')
            for j in range(i, n):
                if isPalindrome(i, j):
                    groups = min(groups, 1 + dfs(j+1))
            return groups

        return dfs(0)-1

# https://www.youtube.com/watch?v=o6znq56UGL8
class SolutionBottomUp:
    def minCut(self, s: str) -> int: 
        @functools.lru_cache(None)
        def isPalindrome(l, r): # [l, r], both inclusive
            # return s[l:r+1] == s[l:r+1][::-1] # SLOW
            
            # SLOW
            # while l < r:
            #     if s[l] != s[r]: return False
            #     l+=1
            #     r-=1
            # return True
            
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        n = len(s)
        dp = [float("inf")] * n
        dp[0] = 1
        
        # dp[i] = numbers of palindrome for s[:i], i inclusive
        for i in range(0, n):
            for j in range(0, i+1):
                if isPalindrome(j, i):
                    if j == 0:
                        dp[i] = 1 # s[j:i] is palindrome
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
        
        return dp[n-1]-1

"""
check Leetcode 647. Palindromic Substrings
we can also precompute and check if every substring is palindrome by dynamic programming.

if nested substring s[start+1][end-1] is palindrome and s[start] == s[end],
then s[start][end] is also a palindrome
"""
class SolutionOptimized:
    def minCut(self, s: str) -> int: 
        n = len(s)
        
        # definition: isPalindrome[start][end] = is s[start:end] a palindrome or not,  both start, end are inclusive
        isPalindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            isPalindrome[i][i] = True # single letter is palindrome
            
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end]:
                    if end-start+1 <= 3 or isPalindrome[start+1][end-1]: # a or aa or aba or nested substring is palindrome and s[start] == s[end]
                        isPalindrome[start][end] = True
        
        
        dp = [float("inf")] * n
        dp[0] = 1 # single letter is also palindrome
        
        # dp[i] = numbers of palindrome for s[:i], i inclusive
        for i in range(0, n):
            for j in range(0, i+1):
                if isPalindrome[j][i]:
                    if j == 0: # j == 0 and s[j:i] is palindrome => total substring is palindrome, number of palindrome is 1
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], dp[j-1]+1)
        
        return dp[n-1]-1