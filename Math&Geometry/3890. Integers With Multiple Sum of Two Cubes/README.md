[3890. Integers With Multiple Sum of Two Cubes](https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/)

`Medium`

You are given an integer n.

An integer x is considered good if there exist at least two distinct pairs (a, b) such that:

- a and b are positive integers.
- a <= b
- x = a3 + b3
Return an array containing all good integers less than or equal to n, sorted in ascending order.


Example 1:
Input: n = 4104
Output: [1729,4104]
Explanation:
Among integers less than or equal to 4104, the good integers are:

1729: 13 + 123 = 1729 and 93 + 103 = 1729.
4104: 23 + 163 = 4104 and 93 + 153 = 4104.
Thus, the answer is [1729, 4104].

Example 2:
Input: n = 578
Output: []
Explanation:
There are no good integers less than or equal to 578, so the answer is an empty array.


Constraints:

- 1 <= n <= $10^9$
 
Accepted
26,145/46.6K
Acceptance Rate
56.1%

<details>
<summary>Hint 1</summary>

Iterate over all pairs (a, b) with a <= b and a3 + b3 <= n

</details>
<details>
<summary>Hint 2</summary>

Use a map to count how many times each value of a3 + b3 appears

</details>
<details>
<summary>Hint 3</summary>

A value is good if it can be formed by at least two distinct pairs

</details>
<details>
<summary>Hint 4</summary>

Collect all such values and return them in sorted order

</details>