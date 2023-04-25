[1745. Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv/)

`Hard`

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

```
Example 1:
Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

Example 2:
Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
``` 

Constraints:

- 3 <= s.length <= 2000
- s​​​​​​ consists only of lowercase English letters.

Acceptance Rate
45.3%

<details>
<summary>Hint 1</summary>

Preprocess checking palindromes in O(1)

</details>

<details>
<summary>Hint 2</summary>

Note that one string is a prefix and another one is a suffix you can try brute forcing the rest

</details>

<details>
<summary>Video Explanation in Chinese</summary>

[HuifengGuan](https://www.youtube.com/watch?v=fBxGmOLmlyU)
</details>