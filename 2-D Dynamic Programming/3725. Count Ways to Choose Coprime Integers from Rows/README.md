[3725. Count Ways to Choose Coprime Integers from Rows](https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/)

`Hard`

You are given a m x n matrix mat of positive integers.

Return an integer denoting the number of ways to choose exactly one integer from each row of mat such that the greatest common divisor of all chosen integers is 1.

Since the answer may be very large, return it modulo $10^9$ + 7.

```
Example 1:
Input: mat = [[1,2],[3,4]]
Output: 3
Explanation:

Chosen integer in the first row	Chosen integer in the second row	Greatest common divisor of chosen integers
1	3	1
1	4	1
2	3	1
2	4	2
3 of these combinations have a greatest common divisor of 1. Therefore, the answer is 3.

Example 2:
Input: mat = [[2,2],[2,2]]
Output: 0
Explanation:

Every combination has a greatest common divisor of 2. Therefore, the answer is 0.
```

Constraints:

- 1 <= m == mat.length <= 150
- 1 <= n == mat[i].length <= 150
- 1 <= mat[i][j] <= 150
 

Accepted
6,119/13.2K
Acceptance Rate
46.5%

<details>
<summary>Hint 1</summary>

Use dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Use dp[row][g], where row is the current row and g is the current gcd value.

</details>
<details>
<summary>Hint 3</summary>

Initialize the first row: for each value v in row 0 do dp[0][v] += 1.

</details>
<details>
<summary>Hint 4</summary>

For a row i, use the values from the previous row i - 1 to build the values: for each previous gcd g and each value v in row i.

</details>
<details>
<summary>Hint 5</summary>

The final answer is dp[n-1][1] (number of ways with gcd 1).

</details>