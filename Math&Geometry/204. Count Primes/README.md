[204. Count Primes](https://leetcode.com/problems/count-primes/)

`Medium`

Given an integer n, return the number of prime numbers that are strictly less than n.

```
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
```

Constraints:

- 0 <= n <= 5 * 10^6

<details>
<summary>Hint 1</summary>

Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
</details>

<details>
<summary>Hint 2</summary>

Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
</details>

<details>
<summary>Hint 3</summary>

Use Sieve of Eratosthenes.
</details>

<details>
<summary>Explanation</summary>

[如何高效搜尋質數](https://labuladong.github.io/algo/4/32/116/)
</details>