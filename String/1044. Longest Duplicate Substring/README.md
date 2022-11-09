1044. Longest Duplicate Substring

*SUBSCRIBE TO UNLOCK*

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
Constraints:

- 2 <= s.length <= 3 * 10^4
- s consists of lowercase English letters.

<details>
<summary>Hint</summary>

TLE if we use dynamic programming would be O(n^2)

dp[i][j] = dp[i-1][j-1]+1 if s[i] == s[j] else 0
max(dp[i][j])

Try [Rolling Hash](https://labuladong.github.io/algo/2/20/28/) with binary search

[video explanation](https://www.youtube.com/watch?v=N7EE0VamNqc&ab_channel=HuifengGuan)
[article explanation](https://www.cnblogs.com/grandyang/p/14497723.html)
</details>