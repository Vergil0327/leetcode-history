[3240. Minimum Number of Flips to Make Binary Grid Palindromic II](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/)

`Medium`

You are given an m x n binary matrix grid.

A row or column is considered palindromic if its values read the same forward and backward.

You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

Return the minimum number of cells that need to be flipped to make all rows and columns palindromic, and the total number of 1's in grid divisible by 4.

Example 1:
Input: grid = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation:

```
100    101
010 => 000
001    101
```

Example 2:
Input: grid = [[0,1],[0,1],[0,0]]
Output: 2
Explanation:

```
01    00
01 => 00
00    00
```

Example 3:
Input: grid = [[1],[1]]
Output: 2
Explanation:

```
1    0
1 => 0
```

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m * n <= 2 * 10^5
- 0 <= grid[i][j] <= 1

Accepted
6.7K
Submissions
34.8K
Acceptance Rate
19.4%

<details>
<summary>Hint 1</summary>

For each (x, y), find (m - 1 - x, y), (m - 1 - x, n - 1 - y), and (x, n - 1 - y); they should be the same.

</details>
<details>
<summary>Hint 2</summary>

Note that we need to specially handle the middle row (column) if the number of rows (columns) is odd.

</details>