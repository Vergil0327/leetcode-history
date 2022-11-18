[1201. Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)

`Medium`

An ugly number is a positive integer that is divisible by a, b, or c.

Given four integers n, a, b, and c, return the nth ugly number.

```
Example 1:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Example 2:
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Example 3:
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
```

Constraints:

- 1 <= n, a, b, c <= 10^9
- 1 <= a * b * c <= 10^18
- It is guaranteed that the result will be in range [1, 2 * 10^9].

<details>
<summary>Hint 1</summary>

Write a function f(k) to determine how many ugly numbers smaller than k. As f(k) is non-decreasing, try binary search.
</details>

<details>
<summary>Hint 2</summary>

Find all ugly numbers in [1, LCM(a, b, c)] (LCM is Least Common Multiple). Use inclusion-exclusion principle to expand the result.
</details>

<details>
<summary>Explanation</summary>
[Huifeng Guan - 1201. Ugly Number III](https://www.youtube.com/watch?v=60PyXFrEf44)
[丑数系列算法](https://mp.weixin.qq.com/s/XXsWwDml_zHiTEFPZtbe3g)
</details>