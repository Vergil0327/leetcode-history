[3983. Subsequence After One Replacement](https://leetcode.com/problems/subsequence-after-one-replacement/)

`Medium`

You are given two strings s and t consisting of lowercase English letters.

You may choose at most one index in s and replace the character at that index with any lowercase English letter.

Return true if it is possible to make s a subsequence of t; otherwise, return false.


Example 1:
Input: s = "cat", t = "chat"
Output: true
Explanation:
Replace s[1] from 'a' to 'h'. The resulting string is "cht".
"cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.

Example 2:
Input: s = "plane", t = "apple"
Output: false
Explanation:
The characters 'p', 'l', and 'e' can be matched in t, but the remaining characters cannot be matched while preserving the required order.
Even after replacing any one character in s, it is impossible to make s a subsequence of t.


Constraints:

- 1 <= s.length, t.length <= $10^5$
- s and t consist only of lowercase English letters.

Accepted
14,440/69.4K
Acceptance Rate
20.8%

<details>
<summary>Hint 1</summary>

If s.length > t.length, the answer is false.


</details>
<details>
<summary>Hint 2</summary>

First check whether s is already a subsequence of t.

</details>
<details>
<summary>Hint 3</summary>

For each index i in s, compute the earliest position in t after matching s[0..i-1], and the latest position in t before matching s[i+1..s.length - 1].

</details>
<details>
<summary>Hint 4</summary>

Try each index i of s as the character to replace. The characters before i and after i must still be matchable in order inside t, with at least one unused position between them for the replaced character.

</details>