[3844. Longest Almost-Palindromic Substring](https://leetcode.com/problems/longest-almost-palindromic-substring/)

`Medium`

You are given a string s consisting of lowercase English letters.

A substring is almost-palindromic if it becomes a palindrome after removing exactly one character from it.

Return an integer denoting the length of the longest almost-palindromic substring in s.


Example 1:
Input: s = "abca"
Output: 4
Explanation:

Choose the substring "abca".

Remove "abca".
The string becomes "aba", which is a palindrome.
Therefore, "abca" is almost-palindromic.

Example 2:
Input: s = "abba"
Output: 4
Explanation:

Choose the substring "abba".

Remove "abba".
The string becomes "aba", which is a palindrome.
Therefore, "abba" is almost-palindromic.

Example 3:
Input: s = "zzabba"
Output: 5
Explanation:
Choose the substring "zzabba".

Remove "zabba".
The string becomes "abba", which is a palindrome.
Therefore, "zabba" is almost-palindromic.
 

Constraints:

- 2 <= s.length <= 2500
- s consists of only lowercase English letters.
 

Accepted
12,613/58.7K
Acceptance Rate
21.5%

<details>
<summary>Hint 1</summary>

Solve greedily

</details>
<details>
<summary>Hint 2</summary>

Fix the center (consider both odd and even centers) and expand outwards

</details>
<details>
<summary>Hint 3</summary>

On the first mismatch, try skipping the left character and continue expanding, and also try skipping the right character; take the longer result

</details>
<details>
<summary>Hint 4</summary>

Track the maximum length found across all centers

</details>