# [solution from @lee215](https://leetcode.com/problems/longest-almost-palindromic-substring/solutions/7580116/javacpython-center-expansion-by-lee215-oxto)
# Explanation
# It iterates through all possible centers for palindromes.
# For each center, it first expands while characters match.
# During this, it considers substrings with one extra char.

# When a mismatch occurs, it tries two possibilities:
# Skip the character on the left side.
# Skip the character on the right side.

# It then continues expanding as a perfect palindrome.
# The maximum length found across all centers is tracked.
# The result is capped by the original string length.

class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        res = 0

        # odd center
        for i in range(n):
            # expand valid palindrome first
            j = i
            while i >= 0 and j < n and s[i] == s[j]:
                length = j - i + 1
                res = max(res, length + 1) # plus one more character if we haven't remove any character yet
                i, j = i - 1, j + 1

            # try removing left
            l, r = i - 1, j
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                res = max(res, length)
                l -= 1
                r += 1

            # try removing right
            l, r = i, j + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                res = max(res, length)
                l -= 1
                r += 1
        
        # even center
        for i in range(n):
            # expand valid palindrome first
            j = i + 1
            while i >= 0 and j < n and s[i] == s[j]:
                length = j - i + 1
                res = max(res, length + 1) # plus one more character if we haven't remove any character yet
                i, j = i - 1, j + 1

            # try removing left
            l, r = i - 1, j
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                res = max(res, length)
                l, r = l - 1, r + 1

            # try removing right
            l, r = i, j + 1
            while l >= 0 and r < n and s[l] == s[r]:
                length = r - l + 1
                res = max(res, length)
                l, r = l - 1, r + 1
        return min(res, n)