[1316. Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings/)

`Hard`

Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

```
Example 1:
Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".

Example 2:
Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
``` 

Constraints:

- 1 <= text.length <= 2000
- text has only lowercase English letters.

Acceptance Rate
49.6%

<details>
<summary>Hint 1</summary>

Given a substring of the text, how to check if it can be written as the concatenation of a string with itself ?

</details>

<details>
<summary>Hint 2</summary>

We can do that in linear time, a faster way is to use hashing.

</details>

<details>
<summary>Hint 3</summary>

Try all substrings and use hashing to check them.

</details>

<details>
<summary>Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=JgUJuE5tyd4&ab_channel=HuifengGuan)
</details>