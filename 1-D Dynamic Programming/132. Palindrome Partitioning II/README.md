[132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)

`Hard`

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

```
Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
```

Constraints:

- 1 <= s.length <= 2000
- s consists of lowercase English letters only.

<details>
<summary>Explanation</summary>

https://www.youtube.com/watch?v=o6znq56UGL8
</details>

<details>
<summary>Most Efficient Solution</summary>

```python
# 441 ms
class Solution:
    def minCut(self, s):
        # acceleration
        if s == s[::-1]: return 0

        # algorithm
        cut = [x for x in range(-1,len(s))] # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]
```
</details>