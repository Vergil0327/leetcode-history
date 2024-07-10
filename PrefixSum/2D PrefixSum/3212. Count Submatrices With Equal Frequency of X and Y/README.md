[3212. Count Submatrices With Equal Frequency of X and Y](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/)

`Medium`

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contains:

- grid[0][0]
- an equal frequency of 'X' and 'Y'.
- at least one 'X'.
 
```
Example 1:
Input: grid = [["X","Y","."],["Y",".","."]]
Output: 3

Example 2:
Input: grid = [["X","X"],["X","Y"]]
Output: 0
Explanation:
No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:
Input: grid = [[".","."],[".","."]]
Output: 0
Explanation:
No submatrix has at least one 'X'.
```

Constraints:

- 1 <= grid.length, grid[i].length <= 1000
- grid[i][j] is either 'X', 'Y', or '.'.

Accepted
17.9K
Submissions
35.8K
Acceptance Rate
49.9%

<details>
<summary>Hint 1</summary>

Replace ’X’ with 1, ’Y’ with -1 and ’.’ with 0.

</details>
<details>
<summary>Hint 2</summary>

You need to find how many submatrices grid[0..x][0..y] have a sum of 0 and at least one ’X’.

</details>
<details>
<summary>Hint 3</summary>

Use prefix sum to calculate submatrices sum.

</details>