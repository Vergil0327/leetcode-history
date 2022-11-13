
# O(n^2), Runtime: 5519 ms, faster than 8.33%
class SolutionBruteForce:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = [] # [l, r] means valid palindrome s[l:r] both inclusive
        for i in range(n):
            l = r = i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 >=k:
                    intervals.append([l, r])
                l, r = l-1, r+1
                
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 >=k:
                    intervals.append([l, r])
                l, r = l-1, r+1
        
        # now the problem become "Find Maximum Number of Non-overlapping Interval"
        
        # Greedy
        # if l in [l, r] larger than previous r', it's valid count
        # if l in [l, r] is smaller than prevoius r' and r is also smaller than r', we can replace previous one
        # -> which means we can update previous r' to r
        res = []
        intervals.sort()
        for l, r in intervals:
            if not res or l > res[-1][1]:
                res.append([l, r])
            elif r < res[-1][1]:
                res[-1][1] = r
        
        return len(res)

# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/discuss/2808805/C%2B%2B-Java-Python3-Palindromic-Substrings-%2B-Non-overlapping-Intervals
# Explanation
# This question is a combination of Palindromic Substring and Non-overlapping intervals
# https://leetcode.com/problems/palindromic-substrings/
# https://leetcode.com/problems/non-overlapping-intervals/

# Algorithm:
#   1. First find all palindromic substrings with length >= k in O(n*k) and store their start and end in an intervals list
#   2. Then find minumum number of intervals you need to remove to make the intervals array non overlapping in O(n) (intervals is already added in sorted order.)
# Runtime: 106 ms, faster than 83.33% of Python3
class GreedySolution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # ! Really Clever Way to Find Palindrome In Sorted Order
        intervals = [] # [l, r] means valid palindrome s[l:r] both inclusive
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                # !!! Greedy, once we found valid, we end the search.
                # the shorter palindrome is, the higher chance we get maximum number of palindromes
                if right + 1 - left >= k:
                    intervals.append((left, right))
                    break
                left -= 1
                right += 1
        
        # now the problem become "Find Maximum Number of Non-overlapping Interval"
        
        # ! Greedy
        # if l in [l, r] larger than previous r', it's valid count
        # if l in [l, r] is smaller than prevoius r' and r is also smaller than r', we can replace previous one
        # -> which means we can update previous r' to r
        res = []
        for l, r in intervals:
            if not res or l > res[-1][1]:
                res.append([l, r])
            elif r < res[-1][1]:
                res[-1][1] = r
        
        return len(res)
