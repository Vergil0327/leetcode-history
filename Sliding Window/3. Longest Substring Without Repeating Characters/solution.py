# https://labuladong.github.io/algo/1/12/
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict(lambda: 0)
        
        longest = 0
        l, r = 0, 0
        while r < len(s):
            ch = s[r]
            r+=1
            visited[ch] += 1
            
            while visited[ch] > 1:
                visited[s[l]] -= 1
                l+=1

            longest = max(longest, r-l)

        return longest
