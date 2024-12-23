[1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/)

`Medium`

Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

- i - k <= r <= i + k,
- j - k <= c <= j + k, and
- (r, c) is a valid position in the matrix.
 
```
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
``` 

Constraints:

- m == mat.length
- n == mat[i].length
- 1 <= m, n, k <= 100
- 1 <= mat[i][j] <= 100

Accepted
93.6K
Submissions
123.6K
Acceptance Rate
75.7%

<details>
<summary>Hint 1</summary>

How to calculate the required sum for a cell (i,j) fast ?

</details>
<details>
<summary>Hint 2</summary>

Use the concept of cumulative sum array.

</details>
<details>
<summary>Hint 3</summary>

Create a cumulative sum matrix where dp[i][j] is the sum of all cells in the rectangle from (0,0) to (i,j), use inclusion-exclusion idea.

</details>