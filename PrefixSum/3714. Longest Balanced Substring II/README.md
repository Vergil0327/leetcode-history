[3714. Longest Balanced Substring II](https://leetcode.com/problems/longest-balanced-substring-ii/)

`Medium`

You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

```
Example 1:
Input: s = "abbac"
Output: 4
Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:
Input: s = "aabcc"
Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:
Input: s = "aba"
Output: 2
Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
```

Constraints:

- 1 <= s.length <= $10^5$
- s contains only the characters 'a', 'b', and 'c'.
 

Accepted
4,480/29.8K
Acceptance Rate
15.0%

<details>
<summary>Hint 1</summary>

Solve for three cases: all-equal characters, exactly two distinct characters, and all three characters present. Treat each case separately and take the maximum length.

</details>
<details>
<summary>Hint 2</summary>

Case 1: single character: the longest balanced substring is the longest run of the same character; report its length.

</details>
<details>
<summary>Hint 3</summary>

Case 2: two distinct characters: reduce to that pair (ignore the third character) and use prefix differences of their counts; equal counts between two indices mean the substring between them is balanced for those two chars.

</details>
<details>
<summary>Hint 4</summary>

Case 3: all three characters: use prefix counts and hash the pair `(count_b - count_a, count_c - count_a)` for each prefix; if the same pair appears at two indices the substring between them has equal counts for a, b, and c. Store earliest index per pair to get maximal length.

</details>