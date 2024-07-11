[1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

`Medium`

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

```
Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
``` 

Constraints:

- 1 <= s.length <= 2000
- s only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.

Accepted
79.7K
Submissions
118.8K
Acceptance Rate
67.1%

<details>
<summary>Hint 1</summary>

Find all brackets in the string.

</details>
<details>
<summary>Hint 2</summary>

Does the order of the reverse matter ?

</details>
<details>
<summary>Hint 3</summary>

The order does not matter.

</details>