[1542. Find Longest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/)

Hard

You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

Return the length of the maximum length awesome substring of s.

```
Example 1:
Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

Example 2:
Input: s = "12345678"
Output: 1

Example 3:
Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
``` 

Constraints:

- 1 <= s.length <= 10^5
- s consists only of digits.

Accepted
12.8K
Submissions
30.1K
Acceptance Rate
42.6%

<details>
<summary>Hint 1</summary>

Given the character counts, under what conditions can a palindrome be formed ?

</details>
<details>
<summary>Hint 2</summary>

From left to right, use bitwise xor-operation to compute for any prefix the number of times modulo 2 of each digit. (mask ^= (1<<(s[i]-'0')).

</details>
<details>
<summary>Hint 3</summary>

Expected complexity is O(n*A) where A is the alphabet (10).

</details>