[926. Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/description/)

`Medium`

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

```
Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
```

Constraints:

- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.

<details>
<summary>Official Solution</summary>

Approach 1: Dynamic Windows
Intuition
The result monotone increasing string can be considered as 2 consecutive non-overlapping substrings, namely, the prefix only contains character '0' and the suffix only contains character '1'. Let's consider the 2 substrings as 2 windows on the original string. Initially, the left window is empty and the right window contains the whole string. At each step, the left window's size increases by one and the right window's size decreases by 1. We want to change all the characters in the left window into '0' and all the characters in the right window into '1'.

Algorithm
We enumerate each left-right window configuration, the number of flips to make the string monotone increasing is the sum of the number of '1's in the left window and the number of '0's in the right window. Save the smallest value.


For example, in the above configuration, the number of flips to make the string monotone increasing is 4 (flip the 4 '1's in the left/green window) + 3 (flip the 3 '0's in the right/red window) = 7.

Let left1 be the number of '1's in the current left window and right0 be the number of '0's in the current right window. When the left window increases and the right window shrinks by 1 character, it means we move a character c from right to left:

If c = '0', left1 will be unchanged and right0 will be decreased by 1, so the sum of them will be decreased by 1.

If c = '1', left1 will be increased by 1 and right0 will be unchanged so the sum of them will be increased by 1.

We only need to know the result of left1 + right0, so we don't need to maintain the 2 counters separately. We can use a variable m where m = left1 + right0 implicitly.

The algorithm works as follows:

Scan the input string s to count the number of '0's in total, let it be m. This is the number of flips needed when the left window is empty and the right window is the whole string.
Set ans = m.
Scan the input string 's' again,
for each character '0', decrease m by 1 and replace ans with m if m is smaller.
for each character '1', increase m by 1.
Return ans.

```py
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == '0':
                m += 1
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans
```
</details>