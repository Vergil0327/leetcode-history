[4022. K-th Digit in Infinite String](https://leetcode.com/problems/k-th-digit-in-infinite-string/)

`Medium`

You are given an integer k.

An infinite string is formed by concatenating the decimal representations of the positive integers, without separators.

For every nonnegative integer b, block b contains the positive integers from 10 * b through 10 * b + 9. The integers in each block are appended as follows:

If b is even, append the integers in increasing order.
If b is odd, append the integers in decreasing order.
Therefore, the string starts with the integers 1 through 9, followed by 19 through 10, then 20 through 29, then 39 through 30, and so on.

Return the kth digit (1-indexed) of this string.


Example 1:
Input: k = 4
Output: 4
Explanation:
The string begins as "123456789..". The 4th digit is '4'.

Example 2:
Input: k = 15
Output: 7
Explanation:
The string begins as "123456789191817..". The 15th digit is '7'.

Example 3:
Input: k = 11
Output: 9
Explanation:
The string begins as "12345678919..". The 11th digit is '9'.

Constraints:

- 1 <= k <= 10^15

<details>
<summary>Hint 1</summary>
The order inside a block does not affect its total number of digits. After finishing block b, the string has used exactly the same number of digits as writing all integers from 1 through 10 * b + 9 in the usual order.
</details>
<details>
<summary>Hint 2</summary>
Write a function that computes the total number of decimal digits needed to write all integers from 1 through x. Compute it by grouping numbers according to their digit length.
</details>
<details>
<summary>Hint 3</summary>
Binary search for the first block b whose cumulative number of digits is at least k. Then subtract the number of digits before that block to obtain the 1-indexed position inside the block.
</details>
<details>
<summary>Hint 4</summary>
For b > 0, all 10 integers in the block have the same number of digits. Use the position inside the block to determine which integer and which digit it refers to. If b is odd, remember that the integers appear in decreasing order.
</details>