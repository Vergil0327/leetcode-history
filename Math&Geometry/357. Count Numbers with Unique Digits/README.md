[357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/)

`Medium`

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

```
Example 1:
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
Input: n = 0
Output: 1
```

Constraints:

- 0 <= n <= 8

<details>
<summary>Hint 1</summary>

A direct way is to use the backtracking approach.

</details>

<details>
<summary>Hint 2</summary>

Backtracking should contains three states which are (the current number, number of steps to get that number and a bitmask which represent which number is marked as visited so far in the current number). Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10n.

</details>

<details>
<summary>Hint 3</summary>

This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.

</details>

<details>
<summary>Hint 4</summary>

Let f(k) = count of numbers with unique digits with length equals k.

</details>

<details>
<summary>Hint 5</summary>

f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].

</details>