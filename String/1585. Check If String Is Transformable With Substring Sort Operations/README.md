[1585. Check If String Is Transformable With Substring Sort Operations](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/)

`Hard`

Given two strings s and t, transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform s into t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.

```
Example 1:
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"

Example 2:
Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"

Example 3:
Input: s = "12345", t = "12435"
Output: false
``` 

Constraints:

- s.length == t.length
- 1 <= s.length <= 10^5
- s and t consist of only digits.

Accepted
7.8K
Submissions
16.2K
Acceptance Rate
48.3%

<details>
<summary>Hint 1</summary>

Suppose the first digit you need is 'd'. How can you determine if it's possible to get that digit there?

</details>
<details>
<summary>Hint 2</summary>

Consider swapping adjacent characters to maintain relative ordering.

</details>

<details>
<summary>Explanation by @HuifengGuan in Chinese</summary>

[Link](https://www.youtube.com/watch?v=Rmr1Pn6ws2c)

also mention the original problem in code force

</details>