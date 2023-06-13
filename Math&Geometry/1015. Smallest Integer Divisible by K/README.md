[1015. Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k/description/)

`Medium`

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

```
Example 1:
Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.

Example 2:
Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.

Example 3:
Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
``` 

Constraints:

- 1 <= k <= 10^5

Acceptance Rate
46.8%

<details>
<summary>Hint 1</summary>

11111 = 1111 * 10 + 1 We only need to store remainders modulo K.

</details>

<details>
<summary>Hint 2</summary>

If we never get a remainder of 0, why would that happen, and how would we know that?

</details>