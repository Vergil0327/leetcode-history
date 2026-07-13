[3989. Maximum Consistent Columns in a Grid](https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/)

`Hard`

You are given a 2D integer array grid of size m x n, and an integer limit.

You may remove zero or more columns from the grid, but at least one column must remain. The relative order of the remaining columns must be preserved.

A grid is called consistent if for every row i, and for every pair of adjacent remaining columns a and b with a < b, the following holds: |grid[i][b] - grid[i][a]| <= limit.

Return the maximum number of columns that can remain such that the resulting grid is consistent.


Example 1:
Input: grid = [[-2,0,3]], limit = 2
Output: 2
Explanation:

Remove column 2 and keep columns 0 and 1, which gives |grid[0][1] − grid[0][0]| = |0 − (−2)| = 2 <= limit.
Thus, the maximum number of columns that can remain is 2.

Example 2:
Input: grid = [[1,-1,1],[2,2,2]], limit = 1
Output: 2
Explanation:

Remove column 1 and keep columns 0 and 2, which gives
|grid[0][2] − grid[0][0]| = |1 − 1| = 0 <= limit and
|grid[1][2] − grid[1][0]| = |2 − 2| = 0 <= limit.
Thus, the maximum number of columns that can remain is 2.

Example 3:
Input: grid = [[-5,5]], limit = 9
Output: 1
Explanation:

Remove either column 0 or column 1, since |grid[0][1] − grid[0][0]| = |5 − (−5)| = 10 > limit.
Thus, the maximum number of columns that can remain is 1.
 

Constraints:

- 1 <= m == grid.length <= 250
- 1 <= n == grid[i].length <= 250
- -10^5 <= grid[i][j] <= 10^5
- 0 <= limit <= 10^5​​​​​​​​​​​​​​​​

Accepted
7,336/10.7K
Acceptance Rate
68.5%

<details>
<summary>Hint 1</summary>

Think of each column as one item in a subsequence. Two columns a and b with a < b can be adjacent in the remaining grid only if |grid[i][b] - grid[i][a]| <= limit for every row i.

</details>
<details>
<summary>Hint 2</summary>

Precompute whether every pair of columns (a, b) is compatible.

</details>
<details>
<summary>Hint 3</summary>

Let dp[j] be the maximum number of columns in a valid remaining grid whose last column is j.

</details>
<details>
<summary>Hint 4</summary>

For each j, try all previous columns i < j. If columns i and j are compatible, update dp[j] = max(dp[j], dp[i] + 1).

</details>
<details>
<summary>Hint 5</summary>

The answer is the maximum value of dp[j].

</details>