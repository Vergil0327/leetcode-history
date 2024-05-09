[1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

`Hard`

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

Accepted
68K
Submissions
222.7K
Acceptance Rate
30.5%

<details>
<summary>Hint 1</summary>

Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)

</details>
<details>
<summary>Hint 2</summary>

To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

</details>

<details>
<summary>Hint 3</summary>

TLE if we use dynamic programming would be O(n^2)

dp[i][j] = dp[i-1][j-1]+1 if s[i] == s[j] else 0
max(dp[i][j])

[video explanation](https://www.youtube.com/watch?v=N7EE0VamNqc&ab_channel=HuifengGuan)
[article explanation](https://www.cnblogs.com/grandyang/p/14497723.html)
</details>