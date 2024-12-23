[3399. Smallest Substring With Identical Characters II](https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/)

`Hard`

You are given a binary string s of length n and an integer numOps.

You are allowed to perform the following operation on s at most numOps times:

Select any index i (where 0 <= i < n) and flip s[i]. If s[i] == '1', change s[i] to '0' and vice versa.
You need to minimize the length of the longest substring of s such that all the characters in the substring are identical.

Return the minimum length after the operations.

A substring is a contiguous non-empty sequence of characters within a string.

```
Example 1:
Input: s = "000001", numOps = 1
Output: 2

Explanation: 

By changing s[2] to '1', s becomes "001001". The longest substrings with identical characters are s[0..1] and s[3..4].

Example 2:
Input: s = "0000", numOps = 2
Output: 1
Explanation: 

By changing s[0] and s[2] to '1', s becomes "1010".

Example 3:
Input: s = "0101", numOps = 0
Output: 1
```

Constraints:

- 1 <= n == s.length <= 10^5
- s consists only of '0' and '1'.
- 0 <= numOps <= n

Accepted
2.2K
Submissions
6K
Acceptance Rate
37.2%

<details>
<summary>Hint 1</summary>

Binary search for the answer.

</details>
<details>
<summary>Hint 2</summary>

Group the same digits by size of (`mid + 1`) and ignore any remainder. Flip one in each group (the last one).

</details>
<details>
<summary>Hint 3</summary>

For the last group, we can flip the 2nd last one.

</details>
<details>
<summary>Hint 4</summary>

What if the answer was 1?

</details>
