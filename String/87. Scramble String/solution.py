# daily challenge 2023/03/30

# first, I try to do what algorithm told, and use two index `l`, `r` to define the partition:
# ```
# [X] [X X X] split with no swap
#  l   i   r
# [X X X] [X] split with swap
#  i   r   l
# ```
# then, if I want to check if s1 == s2, I also need to know what part of s2 we should compare for each partition of s1

# so, I add two more index `m`, `n` to define the partition of s2 to keep track of partition of s2.

# since len(s1) equals len(s2), we can use length of partition of s1 and combine with `m`, `n` index to find partition of s2.

# now, we can recursively do the algorithm and compare s1 and s2

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        @lru_cache(None)
        def dfs(l, r, m, n):
            if s1[l:r+1] == s2[m:n+1]: return True
            if l > r or m > n: return False
            
            for i in range(l+1, r+1):
                # x = s[l:i]
                # y = s[i:r+1]
                lenx = i-l
                leny = r+1-i
                
                if dfs(l, i-1, m, m+lenx-1) and dfs(i, r, m+lenx, n): return True
                if dfs(i, r, m, m+leny-1) and dfs(l, i-1, m+leny, n): return True
            return False
        return dfs(0, n-1, 0, n-1)

# Brute Force
class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        
        # Boost Performance, if characters are not matched, it can't be True
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            s1a, s1b = s1[:i], s1[i:]
            for j in range(1, n):
                s2a, s2b = s2[:j], s2[j:]
                if len(s1a) == len(s2a) and len(s1b) == len(s2b):
                    if self.isScramble(s1a, s2a) and self.isScramble(s1b, s2b):
                        return True
                if len(s1a) == len(s2b) and len(s1b) == len(s2a):
                    if self.isScramble(s1a, s2b) and self.isScramble(s1b, s2a):
                        return True
        return False
