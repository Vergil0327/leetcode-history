[3621. Number of Integers With Popcount-Depth Equal to K I](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/)

`Hard`

You are given two integers n and k.

For any positive integer x, define the following sequence:

p0 = x
pi+1 = popcount(pi) for all i >= 0, where popcount(y) is the number of set bits (1's) in the binary representation of y.
This sequence will eventually reach the value 1.

The popcount-depth of x is defined as the smallest integer d >= 0 such that pd = 1.

For example, if x = 7 (binary representation "111"). Then, the sequence is: 7 → 3 → 2 → 1, so the popcount-depth of 7 is 3.

Your task is to determine the number of integers in the range [1, n] whose popcount-depth is exactly equal to k.

Return the number of such integers.

```
Example 1:
Input: n = 4, k = 1
Output: 2
Explanation:

The following integers in the range [1, 4] have popcount-depth exactly equal to 1:

x	Binary	Sequence
2	"10"	2 → 1
4	"100"	4 → 1
Thus, the answer is 2.

Example 2:
Input: n = 7, k = 2
Output: 3
Explanation:

The following integers in the range [1, 7] have popcount-depth exactly equal to 2:

x	Binary	Sequence
3	"11"	3 → 2 → 1
5	"101"	5 → 2 → 1
6	"110"	6 → 2 → 1
Thus, the answer is 3.
```

Constraints:

- 1 <= n <= 10^15
- 0 <= k <= 5

Accepted
2,317/14.7K
Acceptance Rate
15.8%

<details>
<summary>Hint 1</summary>

Use digit dynamic programming on the binary representation of n: let dp[pos][ones][tight] = number of ways to choose bits from the most significant down to position pos with exactly ones ones so far, where tight indicates whether you're still matching the prefix of n.

</details>
<details>
<summary>Hint 2</summary>

Precompute depth[j] for all j from 0 to 64 by repeatedly applying popcount(j) until you reach 1.

</details>
<details>
<summary>Hint 3</summary>

After your DP, let dp_final[j] be the count of numbers <= n that have exactly j ones; the answer is the sum of all dp_final[j] for which depth[j] == k.

</details>