[3563. Lexicographically Smallest String After Adjacent Removals](https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/)

`Hard`

You are given a string s consisting of lowercase English letters.

You can perform the following operation any number of times (including zero):

Remove any pair of adjacent characters in the string that are consecutive in the alphabet, in either order (e.g., 'a' and 'b', or 'b' and 'a').
Shift the remaining characters to the left to fill the gap.
Return the lexicographically smallest string that can be obtained after performing the operations optimally.

Note: Consider the alphabet as circular, thus 'a' and 'z' are consecutive.

```
Example 1:
Input: s = "abc"
Output: "a"
Explanation:

Remove "bc" from the string, leaving "a" as the remaining string.
No further operations are possible. Thus, the lexicographically smallest string after all possible removals is "a".

Example 2:
Input: s = "bcda"
Output: ""
Explanation:

​​​​​​​Remove "cd" from the string, leaving "ba" as the remaining string.
Remove "ba" from the string, leaving "" as the remaining string.
No further operations are possible. Thus, the lexicographically smallest string after all possible removals is "".

Example 3:
Input: s = "zdce"
Output: "zdce"
Explanation:

Remove "dc" from the string, leaving "ze" as the remaining string.
No further operations are possible on "ze".
However, since "zdce" is lexicographically smaller than "ze", the smallest string after all possible removals is "zdce".
```

Constraints:

- 1 <= s.length <= 250
- s consists only of lowercase English letters.

Accepted
1.6K
Submissions
15.9K
Acceptance Rate
10.4%

<details>
<summary>Hint 1</summary>

As a result of the operation, some of the substrings can be removed

</details>
<details>
<summary>Hint 2</summary>

Find out using DP, which substrings can we remove

</details>
<details>
<summary>Hint 3</summary>

Now, try to build the ans using this DP

</details>
<details>
<summary>Hint 4</summary>

Define ans[i] = lexicographically smallest string that can be made in [i, n - 1], then ans[i] = lex_smallest of { choose one char s[j] in [i, n - 1] + ans[j + 1] }

</details>