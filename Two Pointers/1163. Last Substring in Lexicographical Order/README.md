[1163. Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/)

`Hard`

Given a string `s`, return the last substring of `s` in lexicographical order.

```
Example 1:
Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:
Input: s = "leetcode"
Output: "tcode"
``` 

Constraints:

- 1 <= s.length <= 4 * 10^5
- s contains only lowercase English letters.

Acceptance Rate
34.8%

<details>
<summary>Hint 1</summary>

Assume that the answer is a sub-string from index i to j. If you add the character at index j+1 you get a better answer.

</details>

<details>
<summary>Hint 2</summary>

The answer is always a suffix of the given string.

</details>

<details>
<summary>Hint 3</summary>

Since the limits are high, we need an efficient data structure.

</details>

<details>
<summary>Hint 4</summary>

Use suffix array.

</details>