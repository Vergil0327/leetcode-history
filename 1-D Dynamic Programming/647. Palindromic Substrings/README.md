[647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

`Medium`

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

```
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.

<details>
<summary>Hint</summary>

How can we reuse a previously computed palindrome to compute a larger palindrome?
</details>

<details>
<summary>Hint</summary>

If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
</details>

<details>
<summary>Hint</summary>

Complexity based hint:
If we use brute force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?
</details>