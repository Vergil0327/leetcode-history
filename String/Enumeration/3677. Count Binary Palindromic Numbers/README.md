[3677. Count Binary Palindromic Numbers](https://leetcode.com/problems/count-binary-palindromic-numbers/)

`Hard`

You are given a non-negative integer n.

A non-negative integer is called binary-palindromic if its binary representation (written without leading zeros) reads the same forward and backward.

Return the number of integers k such that 0 <= k <= n and the binary representation of k is a palindrome.

Note: The number 0 is considered binary-palindromic, and its representation is "0".

```
Example 1:
Input: n = 9
Output: 6
Explanation:

The integers k in the range [0, 9] whose binary representations are palindromes are:

0 → "0"
1 → "1"
3 → "11"
5 → "101"
7 → "111"
9 → "1001"
All other values in [0, 9] have non-palindromic binary forms. Therefore, the count is 6.

Example 2:
Input: n = 0
Output: 1
Explanation:

Since "0" is a palindrome, the count is 1.
```

Constraints:

- 0 <= n <= $10^15$
 
Accepted
3,714/19.3K
Acceptance Rate
19.2%

<details>
<summary>Hint 1</summary>

Try to think in terms of binary string length rather than brute forcing all numbers <= n.

</details>
<details>
<summary>Hint 2</summary>

How many binary palindromes exist for a given length L? (only the first half determines the whole number.)

</details>
<details>
<summary>Hint 3</summary>

You can pre-count all palindromes of length < len(n) directly using powers of 2.

</details>
<details>
<summary>Hint 4</summary>

For palindromes of length = len(n), extract the prefix of n, mirror it, and check if it exceeds n.

</details>